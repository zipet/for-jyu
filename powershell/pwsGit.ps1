function PwsGit {

Set-Location -LiteralPath ~\ohjelmointi\projects -PassThru;

$status =  git status | Select-Object -Last 1

if ($status -eq "nothing to commit, working tree clean" -Or $status -eq "fatal: not a git repository (or any of the parent directories): .git")
    {
		Write-Output "Nothing to push."
    }
else 
    {
	git add -v * ; 
	$commit = Read-Host "Laita commit viesti: " 
    Write-Output "exit or quit to cancel the commit."
	if ($commit -eq "quit" -Or $commit -eq "exit")
		{
			break
		}
	git commit -am "$commit";
	git push;
    }
}
    