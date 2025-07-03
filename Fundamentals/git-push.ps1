# Git Auto Commit + Pull --rebase + Push Script (dosya seçmeli)

param (
    [string]$message = "Güncelleme yapildi",
    [string[]]$files   # örn: -files "conditions.py","utils/helper.py"
)

Write-Host "Degisiklikler ekleniyor..." -ForegroundColor Cyan

if ($files) {
    # Belirtilen dosyaları ekle
    git add $files
    Write-Host "Sadece su dosyalar eklendi (add fileName): $($files -join ', ')" -ForegroundColor Yellow
}
else {
    # Tüm dosyaları ekle
    git add .
    Write-Host "Tüm degisiklikler eklendi (add .)." -ForegroundColor Yellow
}

Write-Host "Commit islemi yapiliyor: '$message'" -ForegroundColor Green
git commit -m "$message"

Write-Host "Uzaktan degisiklikler cekiliyor (rebase)..." -ForegroundColor Magenta
git pull origin main --rebase

Write-Host "Degisiklikler push ediliyor..." -ForegroundColor Cyan
git push origin main

Write-Host "Tum islemler tamamlandi." -ForegroundColor Cyan
