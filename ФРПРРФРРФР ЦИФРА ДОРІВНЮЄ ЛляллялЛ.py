import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def POMIDOR():
    try:
        x = float(input("введі хіхіхха цифра : "))
        y = float(input("ХАХАХхаХАВІХІх ЧИСЛо у: "))
        logging.info(f"пахає POMIDOR({x}, {y})")
        result = x + y
        logging.info(f"AHAHHA DAAaaaAAaa: {result}")
        return result
    except ValueError as e:
        logging.error(f"kys(норм числа введи йопта): {e}")
        return None
POMIDOR()