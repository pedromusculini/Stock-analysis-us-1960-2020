# PowerShell does not support Python import statements
# If you want to run Python code, use the 'python' command or a script block
# Example:
python -c "
import kagglehub
from kagglehub import KaggleDatasetAdapter
file_path = 'AAPL.csv'
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    'marianadeem755/stock-market-data',
    file_path,
)
print('Primeiros 5 registros:', df.head())
"

# Execute o código Python usando o comando 'python -c'
python -c "
import kagglehub
from kagglehub import KaggleDatasetAdapter
file_path = 'AAPL.csv'
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    'marianadeem755/stock-market-data',
    file_path,
)
print('Primeiros 5 registros:', df.head())
"