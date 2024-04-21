# R is kind of useless shit in modern ML (I guess)
# But I just want to code and be familiar with something new
# So here's a little R block for fov increase😘

print('Hello R!')


# ---------- PACKAGES ----------
# In R we can install and use different packages

install.packages('pacman')  # package manager package
# In this way we install packages

# now after installation we need to
# import it.

require(pacman)  # if we want little notification
library(pacman)  # if we want to import it with no messages


# now we can use pacman to install different packages

pacman::p_load(pacman, dplyr, ggplot2, ggthemes, ggvis,
               httr, lubridate, plotly, rio, rmarkdown,
               shiny, stringr, tidyr, GGally)
# that was fucking ugly...
# but we did it! We installed packages with pacman

# to delete package we can use:

# p_unload(stringr)  here we delete stringr for example