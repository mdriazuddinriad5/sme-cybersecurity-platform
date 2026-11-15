from pathlib import Path
import logging
Path("logs").mkdir(exist_ok=True)
def get_logger(name="sme_cybersecurity"):
    log=logging.getLogger(name)
    if log.handlers: return log
    log.setLevel(logging.INFO)
    fmt=logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    for h in (logging.StreamHandler(), logging.FileHandler("logs/project.log",encoding="utf-8")):
        h.setFormatter(fmt); log.addHandler(h)
    return log
