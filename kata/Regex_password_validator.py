regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*\d)[A-Za-z\d]{6,}$"

"""^               # start of input 
(?=.*?[A-Z])    # Lookahead to make sure there is at least one upper case letter
(?=.*?[a-z])    # Lookahead to make sure there is at least one lower case letter
(?=.*?\d)    # Lookahead to make sure there is at least one number
[A-Za-z\d]{6,} # Make sure there are at least 6 characters of [A-Za-z\d]
$               # end of input
"""