param(
    [string]$path = "./webapp",
    [string]$destinationPath = "./"
)

If (-Not (Test-Path $Path))
{
    Throw "The source directory $path does not exist, please specify an existing directory"
}

$date = Get-Date -Format "dd-MM-yyyy"
$destinationFile = "$($destinationPath + 'backup-' + $date + '.zip')"
if (-Not (Test-Path $destinationFile))
{
    Compress-Archive -Path "./webapp" -CompressionLevel "fastest" -DestinationPath "./backup-$date" 
    Write-Host "Created backup at $('./backup-' + $date + '.zip')"
}
Else
{
    Write-Error "Today's backup already exists"
}
