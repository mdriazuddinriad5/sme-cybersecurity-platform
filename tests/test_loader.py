import pandas as pd, pytest
from src.data.loader import load_csv
def test_valid(tmp_path):
    p=tmp_path/"x.csv"; pd.DataFrame({"x":[1,2],"label":[0,1]}).to_csv(p,index=False)
    assert len(load_csv(p))==2
def test_missing():
    with pytest.raises(FileNotFoundError): load_csv("missing.csv")
