$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $repoRoot 'assets/creation-of-adam.webp'
$output = Join-Path $repoRoot 'assets/creation-of-adam.gif'

# Full pose at t=0. Geometry and fingertip gap stay fixed throughout.
$filter = "scale=960:-1,eq=brightness='0.006*sin(2*PI*t/6)':eval=frame,split[a][b];[a]palettegen=max_colors=96:stats_mode=full[p];[b][p]paletteuse=dither=bayer:bayer_scale=3:diff_mode=rectangle"
& ffmpeg -hide_banner -loglevel error -y -loop 1 -framerate 6 -t 6 -i $source -t 6 -filter_complex $filter -loop 0 $output
if ($LASTEXITCODE -ne 0) { throw 'Hero encoding failed.' }
Write-Output "Encoded assets/creation-of-adam.gif ($((Get-Item $output).Length) bytes)."
