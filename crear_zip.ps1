$zipName = "INSTALADOR_FACTURAS.zip"
$sourceDir = Get-Location
$excludePatterns = @(
    "*.zip", 
    "*.git*", 
    "__pycache__", 
    "*.xlsx", 
    "cache_facturas.json", 
    "reproducir_error.py", 
    "test_repro.xlsx",
    "APPFACTURACION-INSTALACION",
    ".env",
    ".env.example"
)

# Crear lista de archivos a incluir
$filesToZip = Get-ChildItem -Path $sourceDir -Recurse | Where-Object {
    $path = $_.FullName
    $relPath = $path.Substring($sourceDir.Path.Length + 1)
    
    # Excluir basado en patrones
    $exclude = $false
    foreach ($pattern in $excludePatterns) {
        if ($relPath -like $pattern -or $relPath -match $pattern.Replace("*", ".*")) {
            $exclude = $true
            break
        }
    }
    
    # Exluir carpeta FICHEROS/__pycache__
    if ($relPath -like "FICHEROS\__pycache__*") { $exclude = $true }
    
    # Incluir explícitamente solo lo necesario
    if (-not $exclude) {
        return $true
    }
    return $false
}

# Comprimir
Compress-Archive -Path "PROCESAR_FACTURAS.bat", "LANZAR_WEB.bat", "INSTALAR.bat", "README.TXT", "FICHEROS" -DestinationPath $zipName -Force

Write-Host "Zip creado: $zipName"
