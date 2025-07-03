param (
    [string]$message = "",
    [string[]]$files
)

# === 1. Ana klasöre geç ===
$projectPath = "C:\Users\ensko\vscodeProjects\python"
if (-Not (Test-Path $projectPath)) {
    Write-Host "HATA: Belirtilen proje yolu bulunamadi: $projectPath" -ForegroundColor Red
    exit 1
}
Set-Location $projectPath
Write-Host "`n--- Python Klasoru Git Senkronizasyonu Basladi ---`n" -ForegroundColor Blue

# === 2. Dosyaları ekle ===
if ($files) {
    git add $files 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "HATA: Dosya(lar) eklenemedi. Dosya yollarini kontrol et." -ForegroundColor Red
        exit 1
    }
    Write-Host "Belirtilen dosyalar eklendi: $($files -join ', ')" -ForegroundColor Yellow
}
else {
    git add .
    Write-Host "Tum degisiklikler eklendi." -ForegroundColor Yellow
}

# === 3. Commit mesajı boşsa kullanıcıdan al ===
if ([string]::IsNullOrWhiteSpace($message)) {
    $message = Read-Host "Lutfen bir commit mesaji girin"
}

# === 4. Değişiklik var mı kontrol et ===
$pending = git diff --cached --name-only
if (-Not $pending) {
    Write-Host "Uyari: Commit edilecek bir degisiklik yok." -ForegroundColor DarkYellow
    exit 0
}

# === 5. Commit et ===
git commit -m "$message"
if ($LASTEXITCODE -ne 0) {
    Write-Host "HATA: Commit islemi basarisiz oldu." -ForegroundColor Red
    exit 1
}
Write-Host "Commit basarili: '$message'" -ForegroundColor Green

# === 6. Pull --rebase ===
Write-Host "Uzak degisiklikler cekiliyor (pull --rebase)..." -ForegroundColor Blue
git pull origin main --rebase
if ($LASTEXITCODE -ne 0) {
    Write-Host "HATA: Rebase islemi basarisiz oldu. Manuel müdahale gerekebilir." -ForegroundColor Red
    exit 1
}

# === 7. Push ===
Write-Host "Degisiklikler GitHub'a gonderiliyor..." -ForegroundColor Blue
git push origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "HATA: Push islemi basarısız oldu." -ForegroundColor Red
    exit 1
}

# === 8. Tamamlandı ===
Write-Host "`nTum islemler basariyla tamamlandi." -ForegroundColor Green
