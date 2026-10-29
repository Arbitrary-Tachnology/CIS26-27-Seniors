# ==============================
# errors.py -- "Break on purpose"
# ==============================

# -- Warm-up: A program that works
# print("Hello, World!")

#-- Experiment 1: SYNTAX ERROR (translation-time) -----
# print("Hello, World!)

#-- Experiment 2: SYNTAX ERROR ------
# print(Hello, World!)

#-- Experiment 3: Name Error ----------
# Print("Hello, World!")

#-- Experiment 4: Inproper Indentation
# print("Hello")
#    print("World!")

#-- Experiment 5: Zero Division Error------
# print("About to divide")
# print(1 / 0)


#-- Experiment 6: Logic error with numbers -----
# Average of three test scores
# Expected: (90+80+70) / 3 = 80.0
score1 = 90
score2 = 80
score3 = 70

average = (score1 + score2 + score3) / 3
print("Average:", average)
