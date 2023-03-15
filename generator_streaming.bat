@echo off
set contador=0
:loop
if %contador% lss 50 (
    echo Batch: %contador%
    python simulador.py 10000 > dados/dados_sensores.txt     
    echo Arquivo Gerado com Sucesso.
    set /a contador+=1
    timeout /t 30
    goto loop
)
echo off