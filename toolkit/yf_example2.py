
import yfinance as yf
def yf_prc_to_csv(tic,pth,start=None,end=None):
    df = yf.download(tic, start = start, end = end)
    df.to_csv(pth)
if __name__ == "__main__":
    tic = "QAN.AX"
    datadir = '/Users/yangnanquan/Desktop/toolkit/data'
    pth = f'{datadir}/qan_stk_prc.csv'
    yf_prc_to_csv(tic,pth)