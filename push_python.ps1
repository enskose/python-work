param (
    [string]$message = "",
    [string[]]$files
)

# === 1. Ana klasöre geç ===
$projectPath = "C:\Users\ensko\vscodeProjects\python"
if (-Not (Test-Path $projectPath)) {
    Write-Host "HATA: Belirtilen proje yolu bulunamadı: $projectPath" -ForegroundColor Red
    exit 1
}
Set-Location $projectPath
Write-Host "`n--- Python Klasörü Git Senkronizasyonu Başladı ---`n" -ForegroundColor Blue

# === 2. Dosyaları ekle ===
if ($files) {
    git add $files 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "HATA: Dosya(lar) eklenemedi. Dosya yollarını kontrol et." -ForegroundColor Red
        exit 1
    }
    Write-Host "Belirtilen dosyalar eklendi: $($files -join ', ')" -ForegroundColor Yellow
}
else {
    git add .
    Write-Host "Tüm değişiklikler eklendi." -ForegroundColor Yellow
}

# === 3. Commit mesajı boşsa kullanıcıdan al ===
if ([string]::IsNullOrWhiteSpace($message)) {
    $message = Read-Host "Lütfen bir commit mesajı girin"
}

# === 4. Değişiklik var mı kontrol et ===
$pending = git diff --cached --name-only
if (-Not $pending) {
    Write-Host "Uyarı: Commit edilecek bir değişiklik yok." -ForegroundColor DarkYellow
    exit 0
}

# === 5. Commit et ===
git commit -m "$message"
if ($LASTEXITCODE -ne 0) {
    Write-Host "HATA: Commit işlemi başarısız oldu." -ForegroundColor Red
    exit 1
}
Write-Host "Commit başarılı: '$message'" -ForegroundColor Green

# === 6. Pull --rebase ===
Write-Host "Uzak değişiklikler çekiliyor (pull --rebase)..."
git pull origin main --rebase
if ($LASTEXITCODE -ne 0) {
    Write-Host "HATA: Rebase işlemi başarısız oldu. Manuel müdahale gerekebilir." -ForegroundColor Red
    exit 1
}

# === 7. Push ===
Write-Host "Değişiklikler GitHub'a gönderiliyor..."
git push origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "HATA: Push işlemi başarısız oldu." -ForegroundColor Red
    exit 1
}

# === 8. Tamamlandı ===
Write-Host "`nTüm işlemler başarıyla tamamlandı." -ForegroundColor Green
