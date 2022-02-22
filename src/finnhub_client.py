from tkinter.messagebox import NO
import finnhub
import time
import pandas as pd

PERIOD = 30
NUMBER_OF_SAMPLES = 2000


class finnhubCrypto():
    client = None

    def __init__(self) -> None:
        self.client = finnhub.Client(api_key="c8a0o5qad3iasddf68n0")

    def get_candles(
        self, ticker, period=PERIOD,
        n_samples=NUMBER_OF_SAMPLES
    ) -> pd.DataFrame:
        current_time = round(time.time())
        begin_time = current_time - (period * 60 * n_samples)
        return pd.DataFrame.from_dict(
            self.client.crypto_candles(
                ticker, str(period), begin_time, current_time))
