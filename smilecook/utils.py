from passlib.hash import pbkdf2_sha256


def hash_password(password):
    return pbkdf2_sha256.hash(password)

def check_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)





# September:   New Orleans
# October:     Mobile and Tampa
# November:    Fort Myers, FL Keys
# December:    Orlando and Bahamas


# January:     Miami
# February:    Florida Atlantic Coast
# March:       Georgia
# April:       South Carolina

# May:         North Carolina
# June:        Virginia, Delaware, NJ
# July:        NYC       
# August:      CT and RI

# September:   Massachusetts
# October:     Maine
# November:    Philly and DC
# December:    Charlotte and Atlanta

