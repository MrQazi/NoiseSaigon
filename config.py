from selenium.webdriver.common.by import By

PAGE_WAIT = 10
SEE_MORE_WAIT = 2

FUTURE = False
PAST = True

USER_DATA_DIR=r"C:\\Users\\Qazi\AppData\\Local\\Google\\Chrome\\User Data"
USER_PROFILE=r"Default"


AI_KEY="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"
FULL_UPDATE = True

test = ("","")

EVENT_LIST_CONTSAINER = (
    By.XPATH,
    "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[3]"
)

EVENT_LIST_TILE_SELECTOR = (
    By.CSS_SELECTOR,
    "div.x6s0dn4.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1olyfxc.x9f619.x78zum5.x1e56ztr.xyamay9.x1pi30zi.x1l90r2v.x1swvt13.x1gefphp"
)


EVENT_LIST_TILE_URL = (
    By.CSS_SELECTOR,
    "div.x9f619.x1ja2u2z.x78zum5.x1n2onr6.x1r8uery.x1iyjqo2.xs83m0k.xeuugli.x1qughib.x6s0dn4.xozqiw3.x1q0g3np.xykv574.xbmpl8g.x4cne27.xifccgj > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k.xsyo7zv.x16hj40l.x10b6aqq.x1yrsyyn > div > div:nth-child(2) > span > span > div > a"
)

EVENT_PAGE_DETAIL_CONTAINTER = (
    By.XPATH,
    "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div"
)
EVENT_PAGE_TITLE = (
    By.XPATH,
    "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]"
)

EVENT_PAGE_DATETIME = (
    By.XPATH,
    "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]"
)

EVENT_PAGE_VENUE = (
    By.XPATH,
    "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[3]"
)


#mount_0_0_Y5 > div > div > div:nth-child(1) > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.x2lah0s.x1nhvcw1.x1qjc9v5.xozqiw3.x1q0g3np.x78zum5.x1iyjqo2.x1t2pt76.x1n2onr6.x1ja2u2z.x1h6rjhl > div.x9f619.x1n2onr6.x1ja2u2z.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k.x78zum5.x1t2pt76 > div > div > div.x6s0dn4.x78zum5.xdt5ytf.x193iq5w > div > div > div > div > div:nth-child(1) > div
#mount_0_0_Y5 > div > div > div:nth-child(1) > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.x2lah0s.x1nhvcw1.x1qjc9v5.xozqiw3.x1q0g3np.x78zum5.x1iyjqo2.x1t2pt76.x1n2onr6.x1ja2u2z.x1h6rjhl > div.x9f619.x1n2onr6.x1ja2u2z.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k.x78zum5.x1t2pt76 > div > div > div.x6s0dn4.x78zum5.xdt5ytf.x193iq5w > div > div > div > div > div:nth-child(1) > div > div > div > div:nth-child(6) > div > span