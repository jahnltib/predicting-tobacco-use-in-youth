questions = {
    "Artificial_id": "Artificial Unique Identifier",
    "LOCATION": "Where are you currently taking this survey?", # -> Categorical
    "QN1": "How old are you?", # -> Categorical: 0-13, 14-18, 19+
    "QN2": "What is your sex?", # -> Categorical
    "QN3": "What grade are you in?", # -> Categorical: Middle School or High School
    "QN4A": "Are you Hispanic, Latino, Latina, or of Spanish origin? (No, not of Hispanic, Latino, Latina, or Spanish origin)", # REMOVE: to avoid Dummy Variable Trap
    "QN4B": "Are you Hispanic, Latino, Latina, or of Spanish origin? (Yes, Mexican, Mexican American, Chicano, or Chicana)",
    "QN4C": "Are you Hispanic, Latino, Latina, or of Spanish origin? (Yes, Puerto Rican)",
    "QN4D": "Are you Hispanic, Latino, Latina, or of Spanish origin? (Yes, Cuban)",
    "QN4E": "Are you Hispanic, Latino, Latina, or of Spanish origin? (Yes, another Hispanic, Latino, Latina, or Spanish origin)",
    "QN5A": "What race or races do you consider yourself to be? (American Indian or Alaska Native)",
    "QN5B": "What race or races do you consider yourself to be? (Asian)",
    "QN5C": "What race or races do you consider yourself to be? (Black or African American)",
    "QN5D": "What race or races do you consider yourself to be? (Native Hawaiian or Other Pacific Islander)",
    "QN5E": "What race or races do you consider yourself to be? (White)",
    "QN6": "Have you ever used an e-cigarette, even once or twice?",
    "QN7": "How old were you when you first used an e-cigarette, even once or twice?",  # -> Categorical: 0-8, 9-13, 14-18, 19+
    "QN8": "In total, on how many days have you used e-cigarettes in your entire life?", # REMOVE
    "QN9": "During the past 30 days, on how many days did you use e-cigarettes?", # -> Categorical: 0, > 0 (treat them as e-cigarette users or non-users)
    "QN10": "When was the last time you used an e-cigarette, even one or two times?", # REMOVE
    "QN11A": "Why did you first use an e-cigarette? (A friend used them)", # MERGE to NC1 : "Respondent used e-cigarettes due to exposure from friends, media, or family"
    "QN11B": "Why did you first use an e-cigarette? (A family member used them)", # MERGE to NC1 : "Respondent used e-cigarettes due to exposure from friends, media, or family"
    "QN11C": "Why did you first use an e-cigarette? (To try to quit using other tobacco products, such as cigarettes)", # REMOVE
    "QN11D": "Why did you first use an e-cigarette? (They cost less than other tobacco products, such as cigarettes)", # REMOVE
    "QN11E": "Why did you first use an e-cigarette? (They were easier to get than other tobacco products, such as cigarettes)",
    "QN11F": "Why did you first use an e-cigarette? ( I’ve seen people on TV, online, or in movies use them)", # MERGE to NC1 : "Respondent used e-cigarettes due to exposure from friends, media, or family"
    "QN11G": "Why did you first use an e-cigarette? (They are less harmful than other forms of tobacco, such as cigarettes)", # REMOVE
    "QN11H": "Why did you first use an e-cigarette? (They were available in flavors, such as menthol, mint, candy, fruit, or chocolate)", # REMOVE
    "QN11I": "Why did you first use an e-cigarette? (I could use them unnoticed at home or at school)", # REMOVE
    "QN11J": "Why did you first use an e-cigarette? (I could use them to do tricks)", # REMOVE
    "QN11K": "Why did you first use an e-cigarette? (I was curious about them)", # REMOVE
    "QN11L": "Why did you first use an e-cigarette? (I was feeling anxious, stressed, or depressed)",
    "QN11M": "Why did you first use an e-cigarette? (To get a high or buzz from nicotine)", # REMOVE
    "QN11N": "Why did you first use an e-cigarette? (I used them for some other reason)", # REMOVE
    "QN12A": "Why do you currently use e-cigarettes? (A friend uses them)", # MERGE to NC1 : "Respondent used e-cigarettes due to exposure from friends, media, or family"
    "QN12B": "Why do you currently use e-cigarettes? (A family member uses them)", # MERGE to NC1 : "Respondent used e-cigarettes due to exposure from friends, media, or family"
    "QN12C": "Why do you currently use e-cigarettes? (To try to quit using other tobacco products, such as cigarettes)", # REMOVE
    "QN12D": "Why do you currently use e-cigarettes? (They cost less than other tobacco products, such as cigarettes)", # REMOVE
    "QN12E": "Why do you currently use e-cigarettes? (They are easier to get than other tobacco products, such as cigarettes)",
    "QN12F": "Why do you currently use e-cigarettes? ( I’ve seen people on TV, online, or in movies use them)", # MERGE to NC1 : "Respondent used e-cigarettes due to exposure from friends, media, or family"
    "QN12G": "Why do you currently use e-cigarettes? (They are less harmful than other forms of tobacco, such as cigarettes)", # REMOVE
    "QN12H": "Why do you currently use e-cigarettes? (They are available in flavors, such as menthol, mint, candy, fruit, or chocolate)",
    "QN12I": "Why do you currently use e-cigarettes? (I can use them unnoticed at home or at school)", # REMOVE
    "QN12J": "Why do you currently use e-cigarettes? (I can use them to do tricks)", # REMOVE
    "QN12K": "Why do you currently use e-cigarettes? (I am curious about them)", # REMOVE
    "QN12L": "Why do you currently use e-cigarettes? (Because I feel anxious, stressed, or depressed)", # MERGE to NC2: "Respondent has a bad mental state such as anxiety, stress, or depression"
    "QN12M": "Why do you currently use e-cigarettes? (To get a high or buzz from nicotine)", # REMOVE
    "QN12N": "Why do you currently use e-cigarettes? (I use them for some other reason)", # REMOVE
    "QN13": "Which of the following best describes the type of e-cigarette you have used in the past 30 days?", # REMOVE
    "QN14A": "During the past 30 days, what e-cigarette brands did you use? (blu)", # REMOVE
    "QN14B": "During the past 30 days, what e-cigarette brands did you use? (Breeze)", # REMOVE
    "QN14C": "During the past 30 days, what e-cigarette brands did you use? (Elf Bar)", # REMOVE
    "QN14D": "During the past 30 days, what e-cigarette brands did you use? (Esco Bars)", # REMOVE
    "QN14E": "During the past 30 days, what e-cigarette brands did you use? (Fume)", # REMOVE
    "QN14F": "During the past 30 days, what e-cigarette brands did you use? (JUUL)", # REMOVE
    "QN14G": "During the past 30 days, what e-cigarette brands did you use? (HQD)", # REMOVE
    "QN14H": "During the past 30 days, what e-cigarette brands did you use? (Kangvape (including Onee Stick))", # REMOVE
    "QN14I": "During the past 30 days, what e-cigarette brands did you use? (Logic)", # REMOVE
    "QN14K": "During the past 30 days, what e-cigarette brands did you use? (NJOY)", # REMOVE
    "QN14L": "During the past 30 days, what e-cigarette brands did you use? (SMOK (including NOVO))", # REMOVE
    "QN14M": "During the past 30 days, what e-cigarette brands did you use? (Suorin (including Air Bar))", # REMOVE
    "QN14N": "During the past 30 days, what e-cigarette brands did you use? (Vuse)", # REMOVE
    "QN14O": "During the past 30 days, what e-cigarette brands did you use? (Some other brand(s) not listed here)", # REMOVE
    "QN14P": "During the past 30 days, what e-cigarette brands did you use? (Not sure / I don’t know the brand)", # REMOVE
    "QN15": "During the past 30 days, what brand of e-cigarettes did you usually use?", # REMOVE
    "QN16": "Did any of the e-cigarettes that you used in the past 30 days contain nicotine?", # MERGE to NC3: "Respondent used e-cigarettes with nicotine or nicotine salts"
    "QN17": "Did any of the e-cigarettes that you used in the past 30 days contain nicotine salts?", # MERGE to NC3: "Respondent used e-cigarettes with nicotine or nicotine salts"
    "QN18A_A": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Tobacco-flavor)", # REMOVE
    "QN18A_B": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Menthol)", # REMOVE
    "QN18A_C": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Mint)", # REMOVE
    "QN18A_D": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # REMOVE
    "QN18A_E": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Fruit)", # REMOVE
    "QN18A_F": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Chocolate)", # REMOVE
    "QN18A_G": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # REMOVE
    "QN18A_H": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Non-alcoholic drink (such as coffee, soda, lemonade, or other beverage))", # REMOVE
    "QN18A_I": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Candy, desserts, or other sweets)", # REMOVE
    "QN18A_J": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Unflavored)", # REMOVE
    "QN18A_K": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Some other flavor not listed here)", # REMOVE
    "QN18B_A": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Tobacco-flavor)", # REMOVE
    "QN18B_B": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Menthol)", # REMOVE
    "QN18B_C": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Mint)", # REMOVE
    "QN18B_D": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # REMOVE
    "QN18B_E": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Fruit)", # REMOVE
    "QN18B_F": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Chocolate)", # REMOVE
    "QN18B_G": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # REMOVE
    "QN18B_H": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Non-alcoholic drink (such as coffee, soda, lemonade, or other beverage))", # REMOVE
    "QN18B_I": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Candy, desserts, or other sweets)", # REMOVE
    "QN18B_J": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Some other flavor not listed here)", # REMOVE
    "QN18C_A": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Tobacco-flavor)", # REMOVE
    "QN18C_B": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Menthol)", # REMOVE
    "QN18C_C": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Mint)", # REMOVE
    "QN18C_D": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # REMOVE
    "QN18C_E": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Fruit)", # REMOVE
    "QN18C_F": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Chocolate)", # REMOVE
    "QN18C_G": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # REMOVE
    "QN18C_H": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Non-alcoholic drink (such as coffee, soda, lemonade, or other beverage))", # REMOVE
    "QN18C_I": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Candy, desserts, or other sweets)", # REMOVE
    "QN18C_J": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Some other flavor not listed here", # REMOVE
    "QN18D_A": "In the past 30 days when you used snus, what flavors did you use? (Tobacco- flavor)", # REMOVE
    "QN18D_B": "In the past 30 days when you used snus, what flavors did you use? (Menthol)", # REMOVE
    "QN18D_C": "In the past 30 days when you used snus, what flavors did you use? (Mint)", # REMOVE
    "QN18D_D": "In the past 30 days when you used snus, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # REMOVE
    "QN18D_E": "In the past 30 days when you used snus, what flavors did you use? (Fruit)", # REMOVE
    "QN18D_F": "In the past 30 days when you used snus, what flavors did you use? (Chocolate)", # REMOVE
    "QN18D_G": "In the past 30 days when you used snus, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # REMOVE
    "QN18D_H": "In the past 30 days when you used snus, what flavors did you use? (Non- alcoholic drinks (such as coffee, soda, lemonade, or other beverage))", # REMOVE
    "QN18D_I": "In the past 30 days when you used snus, what flavors did you use? (Candy, desserts, or other sweets)", # REMOVE
    "QN18D_J": "In the past 30 days when you used snus, what flavors did you use? (Some other flavor not listed here)", # REMOVE
    "QN18E_A": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Tobacco-flavor)", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_B": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Menthol)", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_C": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Mint)", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_D": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_E": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Fruit)", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_F": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Chocolate)", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_G": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_H": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Non-alcholohic drinks (such as coffee, soda, lemonade, or other beverage))", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_I": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Candy, desserts, or other sweets)", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_J": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Unflavored)", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18E_K": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Some other flavor not listed here)", # MERGE to NC4: "Respondent used nicotine pouches"
    "QN18F_A": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Tobacco-flavor)", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_B": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Menthol)", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_C": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Mint)", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_D": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_E": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Fruit)", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_F": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Chocolate)", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_G": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_H": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Non-alcoholic drinks (such as coffee, soda, lemonade, or other beverage))", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_I": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Candy, desserts, or other sweets)", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_J": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Unflavored)", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18F_K": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Some other flavor not listed here", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN18G_A": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Tobacco-flavor)", # REMOVE
    "QN18G_B": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Menthol)", # REMOVE
    "QN18G_C": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Mint)", # REMOVE
    "QN18G_D": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # REMOVE
    "QN18G_E": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Fruit)", # REMOVE
    "QN18G_F": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Chocolate)", # REMOVE
    "QN18G_G": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # REMOVE
    "QN18G_H": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Non-alcoholic drinks (such as coffee, soda, lemonade, or other beverage))", # REMOVE
    "QN18G_I": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Candy, desserts, or other sweets)", # REMOVE
    "QN18G_J": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Some other flavor not listed here", # REMOVE
    "QN18H_A": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Tobacco-flavor)", # REMOVE
    "QN18H_B": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Menthol)", # REMOVE
    "QN18H_C": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Mint)", # REMOVE
    "QN18H_D": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # REMOVE
    "QN18H_E": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Fruit)", # REMOVE
    "QN18H_F": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Chocolate)", # REMOVE
    "QN18H_G": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # REMOVE
    "QN18H_H": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Non-alcoholic drinks (such as coffee, soda, lemonade, or other beverage))", # REMOVE
    "QN18H_I": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Candy, desserts, or other sweets)", # REMOVE
    "QN18H_J": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Unflavored)", # REMOVE
    "QN18H_K": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Some other flavor not listed here)", # REMOVE
    "QN18I_A": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Tobacco-flavor)", # REMOVE
    "QN18I_B": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Menthol)", # REMOVE
    "QN18I_C": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Mint)", # REMOVE
    "QN18I_D": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # REMOVE
    "QN18I_E": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Fruit)", # REMOVE
    "QN18I_F": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Chocolate)", # REMOVE
    "QN18I_G": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # REMOVE
    "QN18I_H": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Non-alcoholic drinks (such as coffee, soda, lemonade, or other beverages))", # REMOVE
    "QN18I_I": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Candy, desserts, or other sweets)", # REMOVE
    "QN18I_J": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Some other flavor not listed here)", # REMOVE
    "QN18J_A": "In the past 30 days when you used bidis, what flavors did you use? (Tobacco- flavor)", # REMOVE
    "QN18J_B": "In the past 30 days when you used bidis, what flavors did you use? (Menthol)", # REMOVE
    "QN18J_C": "In the past 30 days when you used bidis, what flavors did you use? (Mint", # REMOVE
    "QN18J_D": "In the past 30 days when you used bidis, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # REMOVE
    "QN18J_E": "In the past 30 days when you used bidis, what flavors did you use? (Fruit)", # REMOVE
    "QN18J_F": "In the past 30 days when you used bidis, what flavors did you use? (Chocolate)", # REMOVE
    "QN18J_G": "In the past 30 days when you used bidis, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # REMOVE
    "QN18J_H": "In the past 30 days when you used bidis, what flavors did you use? (Non- alcoholic drinks (such as coffee, soda, lemonade, or other beverages))", # REMOVE
    "QN18J_I": "In the past 30 days when you used bidis, what flavors did you use? (Candy, desserts, or other sweets)", # REMOVE
    "QN18J_J": "In the past 30 days when you used bidis, what flavors did you use? (Some other flavor not listed here)", # REMOVE
    "QN18K_A": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Tobacco-flavor)", # REMOVE
    "QN18K_B": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Menthol)", # REMOVE
    "QN18K_C": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Mint)", # REMOVE
    "QN18K_D": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Spice (such as cinnamon, vanilla, or clove))", # REMOVE
    "QN18K_E": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Fruit)", # REMOVE
    "QN18K_F": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Chocolate)", # REMOVE
    "QN18K_G": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Alcoholic drinks (such as wine, margarita, or other cocktails))", # REMOVE
    "QN18K_H": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Non-alcoholic drinks (such as coffee, soda, lemonade, or other beverages))", # REMOVE
    "QN18K_I": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Candy, desserts, or other sweets)", # REMOVE
    "QN18K_J": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Some other flavor not listed here)", # REMOVE
    "QN19": "Did any of the flavors that you used in the past 30 days have names or descriptions that included the word “ice” or “iced” (for example, blueberry ice or strawberry ice)?", # REMOVE
    "QN20": "Did any of the flavors that you used in the past 30 days have a name that did not describe a specific flavor, such as “solar,” “purple,” “jazz,” “island bash,” “fusion” or some other word or phrase?", # REMOVE
    "QN21A_A": "During the past 30 days, how did you get your e-cigarette devices, pods, cartridges, or e-liquid refills? (I bought them myself)", # MERGE to NC6: "Respondent has had access to e-cigarettes through self-purchase, a friend, or family member"
    "QN21A_B": "During the past 30 days, how did you get your e-cigarette devices, pods, cartridges, or e-liquid refills? (I had someone else buy them for me)", # MERGE to NC6: "Respondent has had access to e-cigarettes through self-purchase, a friend, or family member"
    "QN21A_C": "During the past 30 days, how did you get your e-cigarette devices, pods, cartridges, or e-liquid refills? (I asked someone to give me some)", # MERGE to NC6: "Respondent has had access to e-cigarettes through self-purchase, a friend, or family member"
    "QN21A_D": "During the past 30 days, how did you get your e-cigarette devices, pods, cartridges, or e-liquid refills? (Someone offered them to me)", # MERGE to NC6: "Respondent has had access to e-cigarettes through self-purchase, a friend, or family member"
    "QN21A_E": "During the past 30 days, how did you get your e-cigarette devices, pods, cartridges, or e-liquid refills? (I got them from a friend)", # MERGE to NC6: "Respondent has had access to e-cigarettes through self-purchase, a friend, or family member"
    "QN21A_F": "During the past 30 days, how did you get your e-cigarette devices, pods, cartridges, or e-liquid refills? (I got them from a family member)", # MERGE to NC6: "Respondent has had access to e-cigarettes through self-purchase, a friend, or family member"
    "QN21A_G": "During the past 30 days, how did you get your e-cigarette devices, pods, cartridges, or e-liquid refills? (I took them from a store or another person)", # MERGE to NC6: "Respondent has had access to e-cigarettes through self-purchase, a friend, or family member"
    "QN21A_H": "During the past 30 days, how did you get your e-cigarette devices, pods, cartridges, or e-liquid refills? (I got them in some other way)", # REMOVE
    "QN21B_A": "During the past 30 days, how did you get your cigarettes? (I bought them myself)", # REMOVE
    "QN21B_B": "During the past 30 days, how did you get your cigarettes? (I had someone else buy them for me)", # REMOVE
    "QN21B_C": "During the past 30 days, how did you get your cigarettes? (I asked someone to give me some)", # REMOVE 
    "QN21B_D": "During the past 30 days, how did you get your cigarettes? (Someone offered them to me)", # REMOVE
    "QN21B_E": "During the past 30 days, how did you get your cigarettes? (I got them from a friend)", # REMOVE
    "QN21B_F": "During the past 30 days, how did you get your cigarettes? (I got them from a family member)", # REMOVE
    "QN21B_G": "During the past 30 days, how did you get your cigarettes? (I took them from a store or another person)", # REMOVE
    "QN21B_H": "During the past 30 days, how did you get your cigarettes? (I got them in some other way)", # REMOVE
    "QN21C_A": "During the past 30 days, how did you get your cigars, cigarillos, or little cigars? (I bought them myself)", # REMOVE
    "QN21C_B": "During the past 30 days, how did you get your cigars, cigarillos, or little cigars? (I had someone else buy them for me)", # REMOVE
    "QN21C_C": "During the past 30 days, how did you get your cigars, cigarillos, or little cigars? (I asked someone to give me some)", # REMOVE
    "QN21C_D": "During the past 30 days, how did you get your cigars, cigarillos, or little cigars? (Someone offered them to me)", # REMOVE
    "QN21C_E": "During the past 30 days, how did you get your cigars, cigarillos, or little cigars? (I got them from a friend)", # REMOVE
    "QN21C_F": "During the past 30 days, how did you get your cigars, cigarillos, or little cigars? (I got them from a family member)", # REMOVE
    "QN21C_G": "During the past 30 days, how did you get your cigars, cigarillos, or little cigars? (I took them from a store or another person)", # REMOVE
    "QN21C_H": "During the past 30 days, how did you get your cigars, cigarillos, or little cigars? (I got them in some other way)", # REMOVE
    "QN21D_A": "During the past 30 days, how did you get your chewing tobacco, snuff, or dip? (I bought it myself)", # REMOVE
    "QN21D_B": "During the past 30 days, how did you get your chewing tobacco, snuff, or dip? (I had someone else buy it for me)", # REMOVE
    "QN21D_C": "During the past 30 days, how did you get your chewing tobacco, snuff, or dip? (I asked someone to give me some)", # REMOVE
    "QN21D_D": "During the past 30 days, how did you get your chewing tobacco, snuff, or dip? (Someone offered it to me)", # REMOVE
    "QN21D_E": "During the past 30 days, how did you get your chewing tobacco, snuff, or dip? (I got it from a friend)", # REMOVE
    "QN21D_F": "During the past 30 days, how did you get your chewing tobacco, snuff, or dip? (I got it from a family member)", # REMOVE
    "QN21D_G": "During the past 30 days, how did you get your chewing tobacco, snuff, or dip? (I took it from a store or another person)", # REMOVE
    "QN21D_H": "During the past 30 days, how did you get your chewing tobacco, snuff, or dip? (I got it in some other way)", # REMOVE
    "QN21E_A": "During the past 30 days, how did you get your snus? (I bought it myself)", # REMOVE
    "QN21E_B": "During the past 30 days, how did you get your snus? (I had someone else buy it for me", # REMOVE
    "QN21E_C": "During the past 30 days, how did you get your snus? (I asked someone to give me some)", # REMOVE
    "QN21E_D": "During the past 30 days, how did you get your snus? (Someone offered it to me)", # REMOVE
    "QN21E_E": "During the past 30 days, how did you get your snus? (I got it from a friend)", # REMOVE
    "QN21E_F": "During the past 30 days, how did you get your snus? (I got it from a family member)", # REMOVE
    "QN21E_G": "During the past 30 days, how did you get your snus? (I took it from a store or another person)", # REMOVE
    "QN21E_H": "During the past 30 days, how did you get your snus? (I got it in some other way)", # REMOVE
    "QN21F_A": "During the past 30 days, how did you get your nicotine pouches? (I bought them myself)", # REMOVE
    "QN21F_B": "During the past 30 days, how did you get your nicotine pouches? (I had someone else buy them for me)", # REMOVE
    "QN21F_C": "During the past 30 days, how did you get your nicotine pouches? (I asked someone to give me some)", # REMOVE
    "QN21F_D": "During the past 30 days, how did you get your nicotine pouches? (Someone offered them to me)", # REMOVE
    "QN21F_E": "During the past 30 days, how did you get your nicotine pouches? (I got them from a friend)", # REMOVE
    "QN21F_F": "During the past 30 days, how did you get your nicotine pouches? (I got them from a family member)", # REMOVE
    "QN21F_G": "During the past 30 days, how did you get your nicotine pouches? (I took them from a store or another person)", # REMOVE
    "QN21F_H": "During the past 30 days, how did you get your nicotine pouches? (I got them in some other way)", # REMOVE
    "QN21G_A": "During the past 30 days, how did you get your oral nicotine products? (I bought them myself)", # REMOVE
    "QN21G_B": "During the past 30 days, how did you get your oral nicotine products? (I had someone else buy them for me)", # REMOVE
    "QN21G_C": "During the past 30 days, how did you get your oral nicotine products? (I asked someone to give me some)", # REMOVE
    "QN21G_D": "During the past 30 days, how did you get your oral nicotine products? (Someone offered them to me)", # REMOVE
    "QN21G_E": "During the past 30 days, how did you get your oral nicotine products? (I got them from a friend)", # REMOVE
    "QN21G_F": "During the past 30 days, how did you get your oral nicotine products? (I got them from a family member)", # REMOVE
    "QN21G_G": "During the past 30 days, how did you get your oral nicotine products? (I took them from a store or another person)", # REMOVE
    "QN21G_H": "During the past 30 days, how did you get your oral nicotine products? (I got them in some other way)", # REMOVE
    "QN21H_A": "During the past 30 days, how did you get your hookah tobacco? (I bought it myself)", # REMOVE
    "QN21H_B": "During the past 30 days, how did you get your hookah tobacco? (I had someone else buy it for me)", # REMOVE
    "QN21H_C": "During the past 30 days, how did you get your hookah tobacco? (I asked someone to give me some)", # REMOVE
    "QN21H_D": "During the past 30 days, how did you get your hookah tobacco? (Someone offered it to me)", # REMOVE
    "QN21H_E": "During the past 30 days, how did you get your hookah tobacco? (I got it from a friend)", # REMOVE
    "QN21H_F": "During the past 30 days, how did you get your hookah tobacco? (I got it from a family member)", # REMOVE
    "QN21H_G": "During the past 30 days, how did you get your hookah tobacco? (I took it from a store or another person)", # REMOVE
    "QN21H_H": "During the past 30 days, how did you get your hookah tobacco? (I got it in some other way)", # REMOVE
    "QN21I_A": "During the past 30 days, how did you get your heated tobacco products? (I bought them myself)", # REMOVE
    "QN21I_B": "During the past 30 days, how did you get your heated tobacco products? (I had someone else buy them for me)", # REMOVE
    "QN21I_C": "During the past 30 days, how did you get your heated tobacco products? (I asked someone to give me some", # REMOVE
    "QN21I_D": "During the past 30 days, how did you get your heated tobacco products? (Someone offered them to me)", # REMOVE
    "QN21I_E": "During the past 30 days, how did you get your heated tobacco products? (I got them from a friend)", # REMOVE
    "QN21I_F": "During the past 30 days, how did you get your heated tobacco products? (I got them from a family member)", # REMOVE
    "QN21I_G": "During the past 30 days, how did you get your heated tobacco products? (I took them from a store or another person)", # REMOVE
    "QN21I_H": "During the past 30 days, how did you get your heated tobacco products? (I got them in some other way)", # REMOVE
    "QN21J_A": "During the past 30 days, how did you get your pipe tobacco? (I bought it myself)", # REMOVE
    "QN21J_B": "During the past 30 days, how did you get your pipe tobacco? (I had someone else buy it for me)", # REMOVE
    "QN21J_C": "During the past 30 days, how did you get your pipe tobacco? (I asked someone to give me some)", # REMOVE
    "QN21J_D": "During the past 30 days, how did you get your pipe tobacco? (Someone offered it to me)", # REMOVE
    "QN21J_E": "During the past 30 days, how did you get your pipe tobacco? (I got it from a friend)", # REMOVE
    "QN21J_F": "During the past 30 days, how did you get your pipe tobacco? (I got it from a family member)", # REMOVE
    "QN21J_G": "During the past 30 days, how did you get your pipe tobacco? (I took it from a store or another person)", # REMOVE
    "QN21J_H": "During the past 30 days, how did you get your pipe tobacco? (I got it in some other way)", # REMOVE
    "QN21K_A": "During the past 30 days, how did you get your bidis? (I bought them myself)", # REMOVE
    "QN21K_B": "During the past 30 days, how did you get your bidis? (I had someone else buy them for me)", # REMOVE
    "QN21K_C": "During the past 30 days, how did you get your bidis? (I asked someone to give me some)", # REMOVE
    "QN21K_D": "During the past 30 days, how did you get your bidis? (Someone offered them to me)", # REMOVE
    "QN21K_E": "During the past 30 days, how did you get your bidis? (I got them from a friend)", # REMOVE
    "QN21K_F": "During the past 30 days, how did you get your bidis? (I got them from a family member)", # REMOVE
    "QN21K_G": "During the past 30 days, how did you get your bidis? (I took them from a store or another person)", # REMOVE
    "QN21K_H": "During the past 30 days, how did you get your bidis? (I got them in some other way)", # REMOVE
    "QN21L_A": "During the past 30 days, how did you get your roll-your-own cigarettes? (I bought them myself)", # REMOVE
    "QN21L_B": "During the past 30 days, how did you get your roll-your-own cigarettes? (I had someone else buy them for me)", # REMOVE
    "QN21L_C": "During the past 30 days, how did you get your roll-your-own cigarettes? (I asked someone to give me some", # REMOVE
    "QN21L_D": "During the past 30 days, how did you get your roll-your-own cigarettes? (Someone offered them to me)", # REMOVE
    "QN21L_E": "During the past 30 days, how did you get your roll-your-own cigarettes? (I got them from a friend)", # REMOVE
    "QN21L_F": "During the past 30 days, how did you get your roll-your-own cigarettes? (I got them from a family member)", # REMOVE
    "QN21L_G": "During the past 30 days, how did you get your roll-your-own cigarettes? (I took them from a store or another person)", # REMOVE
    "QN21L_H": "During the past 30 days, how did you get your roll-your-own cigarettes? (I got them in some other way)", # REMOVE
    "QN22A_A": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (I did not buy e-cigarettes during the past 30 days)", # REMOVE
    "QN22A_B": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (I bought them from another person (a friend, family member, or someone else))",  # REMOVE
    "QN22A_C": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (A gas station or convenience store)", # REMOVE
    "QN22A_D": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (A grocery store)", # REMOVE
    "QN22A_E": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (A drugstore)", # REMOVE
    "QN22A_F": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22A_G": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (A vending machine)", # REMOVE
    "QN22A_H": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace)", # REMOVE
    "QN22A_I": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (Through the mail)", # REMOVE
    "QN22A_J": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22A_K": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (A vape shop or tobacco shop)", # REMOVE
    "QN22A_L": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (Some other place not listed here)", # REMOVE
    "QN22B_A": "During the past 30 days, where did you buy your cigarettes? (I did not buy cigarettes during the past 30 days)", # REMOVE
    "QN22B_B": "During the past 30 days, where did you buy your cigarettes? (I bought them from another person (a friend, family member, or someone else))",  # REMOVE
    "QN22B_C": "During the past 30 days, where did you buy your cigarettes? (A gas station or convenience store)", # REMOVE
    "QN22B_D": "During the past 30 days, where did you buy your cigarettes? (A grocery store)", # REMOVE
    "QN22B_E": "During the past 30 days, where did you buy your cigarettes? (A drugstore)", # REMOVE
    "QN22B_F": "During the past 30 days, where did you buy your cigarettes? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22B_G": "During the past 30 days, where did you buy your cigarettes? (A vending machine)", # REMOVE
    "QN22B_H": "During the past 30 days, where did you buy your cigarettes? (On the Internet (such as a product website, online vape or tobacco store or another online marketplace))", # REMOVE
    "QN22B_I": "During the past 30 days, where did you buy your cigarettes? (Through the mail)", # REMOVE
    "QN22B_J": "During the past 30 days, where did you buy your cigarettes? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22B_K": "During the past 30 days, where did you buy your cigarettes? (A vape shop or tobacco shop)", # REMOVE
    "QN22B_L": "During the past 30 days, where did you buy your cigarettes? (Some other place not listed here)", # REMOVE
    "QN22C_A": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (I did not buy cigars, cigarillos, or little cigars during the past 30 days)", # REMOVE
    "QN22C_B": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (I bought them from another person (a friend, family member, or someone else))", # REMOVE
    "QN22C_C": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (A gas station or convenience store)", # REMOVE
    "QN22C_D": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (A grocery store)", # REMOVE
    "QN22C_E": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (A drugstore", # REMOVE
    "QN22C_F": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22C_G": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (A vending machine)", # REMOVE
    "QN22C_H": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (On the Internet (such as a product website, online vape or tobacco store or another online marketplace))", # REMOVE
    "QN22C_I": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (Through the mail)", # REMOVE
    "QN22C_J": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22C_K": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (A vape shop or tobacco shop)", # REMOVE
    "QN22C_L": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (Some other place not listed here)", # REMOVE
    "QN22D_A": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (I did not buy chewing tobacco, snuff, or dip during the past 30 days)", # REMOVE
    "QN22D_B": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (I bought it from another person (a friend, family member, or someone else))", # REMOVE
    "QN22D_C": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (A gas station or convenience store)", # REMOVE
    "QN22D_D": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (A grocery store)", # REMOVE
    "QN22D_E": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (A drugstore)", # REMOVE
    "QN22D_F": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22D_G": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (A vending machine)", # REMOVE
    "QN22D_H": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace))", # REMOVE
    "QN22D_I": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (Through the mail)", # REMOVE
    "QN22D_J": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22D_K": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (A vape shop or tobacco shop)", # REMOVE
    "QN22D_L": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (Some other place not listed here)", # REMOVE
    "QN22E_A": "During the past 30 days, where did you buy your snus? (I did not buy snus during the past 30 days)", # REMOVE
    "QN22E_B": "During the past 30 days, where did you buy your snus? (I bought it from another person (a friend, family member, or someone else))", # REMOVE
    "QN22E_C": "During the past 30 days, where did you buy your snus? (A gas station or convenience store)", # REMOVE
    "QN22E_D": "During the past 30 days, where did you buy your snus? (A grocery store)", # REMOVE
    "QN22E_E": "During the past 30 days, where did you buy your snus? (A drugstore)", # REMOVE
    "QN22E_F": "During the past 30 days, where did you buy your snus? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22E_G": "During the past 30 days, where did you buy your snus? (A vending machine)", # REMOVE
    "QN22E_H": "During the past 30 days, where did you buy your snus? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace))", # REMOVE
    "QN22E_I": "During the past 30 days, where did you buy your snus? (Through the mail)", # REMOVE
    "QN22E_J": "During the past 30 days, where did you buy your snus? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22E_K": "During the past 30 days, where did you buy your snus? (A vape shop or tobacco shop)", # REMOVE
    "QN22E_L": "During the past 30 days, where did you buy your snus? (Some other place not listed here)", # REMOVE
    "QN22F_A": "During the past 30 days, where did you buy your nicotine pouches? (I did not buy nicotine pouches during the past 30 days", # REMOVE
    "QN22F_B": "During the past 30 days, where did you buy your nicotine pouches? (I bought them from another person (a friend, family member, or someone else)", # REMOVE
    "QN22F_C": "During the past 30 days, where did you buy your nicotine pouches? (A gas station or convenience store)", # REMOVE
    "QN22F_D": "During the past 30 days, where did you buy your nicotine pouches? (A grocery store)", # REMOVE
    "QN22F_E": "During the past 30 days, where did you buy your nicotine pouches? (A drugstore)", # REMOVE
    "QN22F_F": "During the past 30 days, where did you buy your nicotine pouches? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22F_G": "During the past 30 days, where did you buy your nicotine pouches? (A vending machine)", # REMOVE
    "QN22F_H": "During the past 30 days, where did you buy your nicotine pouches? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace))", # REMOVE
    "QN22F_I": "During the past 30 days, where did you buy your nicotine pouches? (Through the mail)", # REMOVE
    "QN22F_J": "During the past 30 days, where did you buy your nicotine pouches? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22F_K": "During the past 30 days, where did you buy your nicotine pouches? (A vape shop or tobacco shop)", # REMOVE
    "QN22F_L": "During the past 30 days, where did you buy your nicotine pouches? (Some other place not listed here)", # REMOVE
    "QN22G_A": "During the past 30 days, where did you buy your oral nicotine products? (I did not buy oral nicotine products during the past 30 days)", # REMOVE
    "QN22G_B": "During the past 30 days, where did you buy your oral nicotine products? (I bought them from another person (a friend, family member, or someone else))", # REMOVE
    "QN22G_C": "During the past 30 days, where did you buy your oral nicotine products? (A gas station or convenience store)", # REMOVE
    "QN22G_D": "During the past 30 days, where did you buy your oral nicotine products? (A grocery store)", # REMOVE
    "QN22G_E": "During the past 30 days, where did you buy your oral nicotine products? (A drugstore)", # REMOVE
    "QN22G_F": "During the past 30 days, where did you buy your oral nicotine products? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22G_G": "During the past 30 days, where did you buy your oral nicotine products? (A vending machine)", # REMOVE
    "QN22G_H": "During the past 30 days, where did you buy your oral nicotine products? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace))", # REMOVE
    "QN22G_I": "During the past 30 days, where did you buy your oral nicotine products? (Through the mail)", # REMOVE
    "QN22G_J": "During the past 30 days, where did you buy your oral nicotine products? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22G_K": "During the past 30 days, where did you buy your oral nicotine products? (A vape shop or tobacco shop)", # REMOVE
    "QN22G_L": "During the past 30 days, where did you buy your oral nicotine products? (Some other place not listed here)", # REMOVE
    "QN22H_A": "During the past 30 days, where did you buy your hookah tobacco? (I did not buy hookah tobacco during the past 30 days)", # REMOVE
    "QN22H_B": "During the past 30 days, where did you buy your hookah tobacco? (I bought it from another person (a friend, family member, or someone else))", # REMOVE
    "QN22H_C": "During the past 30 days, where did you buy your hookah tobacco? (A gas station or convenience store)", # REMOVE
    "QN22H_D": "During the past 30 days, where did you buy your hookah tobacco? (A grocery store)", # REMOVE
    "QN22H_E": "During the past 30 days, where did you buy your hookah tobacco? (A drugstore)", # REMOVE
    "QN22H_F": "During the past 30 days, where did you buy your hookah tobacco? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22H_G": "During the past 30 days, where did you buy your hookah tobacco? (A vending machine)", # REMOVE
    "QN22H_H": "During the past 30 days, where did you buy your hookah tobacco? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace))", # REMOVE
    "QN22H_I": "During the past 30 days, where did you buy your hookah tobacco? (Through the mail)", # REMOVE
    "QN22H_J": "During the past 30 days, where did you buy your hookah tobacco? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22H_K": "During the past 30 days, where did you buy your hookah tobacco? (A vape shop or tobacco shop)", # REMOVE
    "QN22H_L": "During the past 30 days, where did you buy your hookah tobacco? (Some other place not listed here)", # REMOVE
    "QN22I_A": "During the past 30 days, where did you buy your heated tobacco products? (I did not buy heated tobacco products during the past 30 days)", # REMOVE
    "QN22I_B": "During the past 30 days, where did you buy your heated tobacco products? (I bought them from another person (a friend, family member, or someone else))", # REMOVE
    "QN22I_C": "During the past 30 days, where did you buy your heated tobacco products? (A gas station or convenience store)", # REMOVE
    "QN22I_D": "During the past 30 days, where did you buy your heated tobacco products? (A grocery store)", # REMOVE
    "QN22I_E": "During the past 30 days, where did you buy your heated tobacco products? (A drugstore)", # REMOVE
    "QN22I_F": "During the past 30 days, where did you buy your heated tobacco products? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22I_G": "During the past 30 days, where did you buy your heated tobacco products? (A vending machine)", # REMOVE
    "QN22I_H": "During the past 30 days, where did you buy your heated tobacco products? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace))", # REMOVE
    "QN22I_I": "During the past 30 days, where did you buy your heated tobacco products? (Through the mail)", # REMOVE
    "QN22I_J": "During the past 30 days, where did you buy your heated tobacco products? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22I_K": "During the past 30 days, where did you buy your heated tobacco products? (A vape shop or tobacco shop)", # REMOVE
    "QN22I_L": "During the past 30 days, where did you buy your heated tobacco products? (Some other place not listed here)", # REMOVE
    "QN22J_A": "During the past 30 days, where did you buy your pipe tobacco? (I did not buy pipe tobacco during the past 30 days)", # REMOVE
    "QN22J_B": "During the past 30 days, where did you buy your pipe tobacco? (I bought it from another person (a friend, family member, or someone else))", # REMOVE
    "QN22J_C": "During the past 30 days, where did you buy your pipe tobacco? (A gas station or convenience store", # REMOVE
    "QN22J_D": "During the past 30 days, where did you buy your pipe tobacco? (A grocery store)", # REMOVE
    "QN22J_E": "During the past 30 days, where did you buy your pipe tobacco? (A drugstore)", # REMOVE
    "QN22J_F": "During the past 30 days, where did you buy your pipe tobacco? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22J_G": "During the past 30 days, where did you buy your pipe tobacco? (A vending machine)", # REMOVE
    "QN22J_H": "During the past 30 days, where did you buy your pipe tobacco? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace))", # REMOVE
    "QN22J_I": "During the past 30 days, where did you buy your pipe tobacco? (Through the mail)", # REMOVE
    "QN22J_J": "During the past 30 days, where did you buy your pipe tobacco? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22J_K": "During the past 30 days, where did you buy your pipe tobacco? (A vape shop or tobacco shop)", # REMOVE
    "QN22J_L": "During the past 30 days, where did you buy your pipe tobacco? (Some other place not listed here)", # REMOVE
    "QN22K_A": "During the past 30 days, where did you buy your bidis? (I did not buy bidis during the past 30 days)", # REMOVE
    "QN22K_B": "During the past 30 days, where did you buy your bidis? (I bought them from another person (a friend, family member, or someone else))", # REMOVE
    "QN22K_C": "During the past 30 days, where did you buy your bidis? (A gas station or convenience store)", # REMOVE
    "QN22K_D": "During the past 30 days, where did you buy your bidis? (A grocery store)", # REMOVE
    "QN22K_E": "During the past 30 days, where did you buy your bidis? (A drugstore)", # REMOVE
    "QN22K_F": "During the past 30 days, where did you buy your bidis? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22K_G": "During the past 30 days, where did you buy your bidis? (A vending machine)", # REMOVE
    "QN22K_H": "During the past 30 days, where did you buy your bidis? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace))", # REMOVE
    "QN22K_I": "During the past 30 days, where did you buy your bidis? (Through the mail)", # REMOVE
    "QN22K_J": "During the past 30 days, where did you buy your bidis? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22K_K": "During the past 30 days, where did you buy your bidis? (A vape shop or tobacco shop)", # REMOVE
    "QN22K_L": "During the past 30 days, where did you buy your bidis? (Some other place not listed here)", # REMOVE
    "QN22L_A": "During the past 30 days, where did you buy your roll-your-own cigarettes? (I did not buy roll-your-own cigarettes during the past 30 days)", # REMOVE
    "QN22L_B": "During the past 30 days, where did you buy your roll-your-own cigarettes? (I bought them from another person (a friend, family member, or someone else))", # REMOVE
    "QN22L_C": "During the past 30 days, where did you buy your roll-your-own cigarettes? (A gas station or convenience store)", # REMOVE
    "QN22L_D": "During the past 30 days, where did you buy your roll-your-own cigarettes? (A grocery store)", # REMOVE
    "QN22L_E": "During the past 30 days, where did you buy your roll-your-own cigarettes? (A drugstore)", # REMOVE
    "QN22L_F": "During the past 30 days, where did you buy your roll-your-own cigarettes? (A mall or shopping center kiosk/stand)", # REMOVE
    "QN22L_G": "During the past 30 days, where did you buy your roll-your-own cigarettes? (A vending machine)", # REMOVE
    "QN22L_H": "During the past 30 days, where did you buy your roll-your-own cigarettes? (On the Internet (such as a product website, online vape or tobacco store or other online marketplace))", # REMOVE
    "QN22L_I": "During the past 30 days, where did you buy your roll-your-own cigarettes? (Through the mail)", # REMOVE
    "QN22L_J": "During the past 30 days, where did you buy your roll-your-own cigarettes? (Through a delivery service (such as DoorDash or Postmates))", # REMOVE
    "QN22L_K": "During the past 30 days, where did you buy your roll-your-own cigarettes? (A vape shop or tobacco shop)", # REMOVE
    "QN22L_L": "During the past 30 days, where did you buy your roll-your-own cigarettes? (Some other place not listed here)", # REMOVE
    "QN23": "How old was this person?", # REMOVE
    "QN24A": "During the past 30 days, which of the following e-cigarette product(s) did you get or buy from another person? (A new e-cigarette device (including disposable devices))",  # REMOVE
    "QN24B": "During the past 30 days, which of the following e-cigarette product(s) did you get or buy from another person? (A pod, cartridge, or e-liquid refill)", # REMOVE
    "QN24C": "During the past 30 days, which of the following e-cigarette product(s) did you get or buy from another person? (A hit or a drag from another person’s e-cigarette device)", # REMOVE
    "QN24D": "During the past 30 days, which of the following e-cigarette product(s) did you get or buy from another person? (Something else)", # REMOVE
    "QN25": "Have you ever purchased an e-cigarette device (including disposable devices), pod, cartridge, single hit, or e-liquid refill while at school or on school property?", # "Respondent has had access to e-cigs at school or on school property"
    "QN26": "During the past 30 days, how often did you use someone else’s e-cigarette device?", # REMOVE
    "QN27": "Are you seriously thinking about quitting e-cigarettes?",
    "QN28": "During the past 12 months, how many times have you stopped using e-cigarettes for one day or longer because you were trying to quit using e-cigarettes for good?", # REMOVE
    "QN29A": "When you tried to quit using e-cigarettes, did you use any of the following? (I did not use any resources)", # REMOVE
    "QN29B": "When you tried to quit using e-cigarettes, did you use any of the following? (Help or advice from a parent or caregiver)", # REMOVE
    "QN29C": "When you tried to quit using e-cigarettes, did you use any of the following? (Help or advice from a friend or peer)", # REMOVE
    "QN29D": "When you tried to quit using e-cigarettes, did you use any of the following? (Help or advice from a teacher or coach)", # REMOVE
    "QN29E": "When you tried to quit using e-cigarettes, did you use any of the following? (Help, advice, or counseling from a doctor or health care provider)", # REMOVE
    "QN29F": "When you tried to quit using e-cigarettes, did you use any of the following? (Treatment from a hospital, medical center, or some other facility)", # REMOVE
    "QN29G": "When you tried to quit using e-cigarettes, did you use any of the following? (Help or advice from the Internet)", # REMOVE
    "QN29H": "When you tried to quit using e-cigarettes, did you use any of the following? (A mobile app or texting program)", # REMOVE
    "QN29I": "When you tried to quit using e-cigarettes, did you use any of the following? (A telephone helpline or Quitline)", # REMOVE
    "QN29J": "When you tried to quit using e-cigarettes, did you use any of the following? (Something else)", # REMOVE
    "QN30": "Have you ever been curious about using an e-cigarette?", # MERGE to NC7: "Respondent has been or is curious about using an e-cigarette"
    "QN31": "Do you think that you will try an e-cigarette soon?", # MERGE to NC7: "Respondent has been or is curious about using an e-cigarette"
    "QN32": "Do you think you will use an e-cigarette in the next year?", # MERGE to NC7: "Respondent has been or is curious about using an e-cigarette"
    "QN33": "If one of your best friends were to offer you an e-cigarette, would you use it?", # MERGE to NC7: "Respondent has been/is curious about using an e-cigarette, or is potentially open to trying one."
    "QN34A": "Have you ever vaped any of the following substances (even once)? (Marijuana (also called pot, weed, or cannabis), including THC, THC concentrates, hash oil, or waxes)", # MERGE to NC8: "Respondent has vaped marijuana, CBD or THC products"
    "QN34B": "Have you ever vaped any of the following substances (even once)? (CBD or CBD oils)", # MERGE to NC8: "Respondent has vaped marijuana, CBD or THC products"
    "QN34C": "Have you ever vaped any of the following substances (even once)? (Synthetic marijuana or cannabinoids, such as K2 or Spice)", # MERGE to NC8: "Respondent has vaped marijuana, CBD or THC products"
    "QN34D": "Have you ever vaped any of the following substances (even once)? (Specify)", # REMOVE
    "QN35A": "Have you vaped any of the following substances during the past 30 days? (Marijuana (also called pot, weed, or cannabis), including THC, THC concentrates, hash oil, or waxes)", # MERGE to NC8: "Respondent has vaped marijuana, CBD or THC products"
    "QN35B": "Have you vaped any of the following substances during the past 30 days? (CBD or CBD oils)", # MERGE to NC8: "Respondent has vaped marijuana, CBD or THC products"
    "QN35C": "Have you vaped any of the following substances during the past 30 days? (Synthetic marijuana or cannabinoids, such as K2 or Spice)", # MERGE to NC8: "Respondent has vaped marijuana, CBD or THC products"
    "QN35D": "Have you vaped any of the following substances during the past 30 days? (Another substance)", # REMOVE
    "QN36": "Have you ever smoked a cigarette, even one or two puffs?", # REMOVE 
    "QN37": "How old were you when you first smoked a cigarette, even one or two puffs?", # -> CATEGORICAL: Smoked a cigarette (atleast once) before age 13, 14-18, 19+
    "QN38": "About how many cigarettes have you smoked in your entire life?", # REMOVE
    "QN39": "During the past 30 days, on how many days did you smoke cigarettes?", # -> CATEGORICAL: 0 or >0 aka "Tobacco User" or "Non-user"
    "QN40": "When was the last time you smoked a cigarette, even one or two puffs?", # REMOVE
    "QN41": "During the past 30 days, on the days you smoked, about how many cigarettes did you smoke per day?", # REMOVE
    "QN42A": "During the past 30 days, what brands of cigarettes did you smoke? (American Spirit)", # REMOVE
    "QN42B": "During the past 30 days, what brands of cigarettes did you smoke? (Camel)", # REMOVE
    "QN42C": "During the past 30 days, what brands of cigarettes did you smoke? (Eagle)", # REMOVE
    "QN42D": "During the past 30 days, what brands of cigarettes did you smoke? (Kool)", # REMOVE
    "QN42E": "During the past 30 days, what brands of cigarettes did you smoke? (Marlboro)", # REMOVE
    "QN42F": "During the past 30 days, what brands of cigarettes did you smoke? (Maverick)", # REMOVE
    "QN42G": "During the past 30 days, what brands of cigarettes did you smoke? (Newport)", # REMOVE
    "QN42H": "During the past 30 days, what brands of cigarettes did you smoke? (L and M)", # REMOVE
    "QN42I": "During the past 30 days, what brands of cigarettes did you smoke? (Lucky Strike)", # REMOVE
    "QN42J": "During the past 30 days, what brands of cigarettes did you smoke? (Pall Mall)", # REMOVE
    "QN42K": "During the past 30 days, what brands of cigarettes did you smoke? (Winston)", # REMOVE
    "QN42L": "During the past 30 days, what brands of cigarettes did you smoke? (Some other brand not listed here)", # REMOVE
    "QN42M": "During the past 30 days, what brands of cigarettes did you smoke? (Not sure / I don’t know the brand", # REMOVE
    "QN43": "During the past 30 days, what brand of cigarettes did you usually smoke?", # REMOVE
    "QN44": "During the past 30 days, were the cigarettes that you usually smoked menthol?", # REMOVE
    "QN46": "Are you seriously thinking about quitting cigarettes?", # REMOVE
    "QN47": "During the past 12 months, how many times have you stopped smoking cigarettes for one day or longer because you were trying to quit smoking cigarettes for good?", # REMOVE
    "QN48": "Have you ever been curious about smoking a cigarette?", # REMOVE , but possibly could combine with more columns
    "QN49": "Do you think that you will try a cigarette soon?",  # REMOVE
    "QN50": "Do you think you will smoke a cigarette in the next year?", # REMOVE
    "QN51": "If one of your best friends were to offer you a cigarette, would you smoke it?", # REMOVE
    "QN52": "Have you ever smoked a cigar, cigarillo, or little cigar, even one or two puffs?", # REMOVE
    "QN53": "How old were you when you first smoked a cigar, cigarillo, or little cigar, even one or two puffs?", # REMOVE
    "QN54": "During the past 30 days, on how many days did you smoke cigars, cigarillos, or little cigars?", # REMOVE
    "QN55": "During the past 30 days, on the days that you smoked, about how many cigars, cigarillos, or little cigars did you smoke per day?", # REMOVE
    "QN56A": "During the past 30 days, which of the following types of cigars have you smoked? (Regular cigars)", # REMOVE
    "QN56B": "During the past 30 days, which of the following types of cigars have you smoked? (Cigarillos)", # REMOVE
    "QN56C": "During the past 30 days, which of the following types of cigars have you smoked? (Little Cigars)", # REMOVE
    "QN56D": "During the past 30 days, which of the following types of cigars have you smoked? (Don’t Know)", # REMOVE
    "QN57A": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Al Capone)", # REMOVE
    "QN57B": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Backwoods)", # REMOVE
    "QN57C": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Cheyenne)", # REMOVE
    "QN57D": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Djarum)", # REMOVE
    "QN57E": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Dutch Masters)", # REMOVE
    "QN57F": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Garcia Y Vega)", # REMOVE
    "QN57G": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Grabba Leaf)", # REMOVE
    "QN57H": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Middleton’s (including Black and Mild))", # REMOVE
    "QN57I": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Optimo)", # REMOVE
    "QN57J": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Phillies)", # REMOVE
    "QN57K": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Swisher Sweets)", # REMOVE
    "QN57L": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (White Owl)", # REMOVE
    "QN57M": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Some other brand not listed here)", # REMOVE
    "QN57N": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Not Sure / I don’t know the brand)", # REMOVE
    "QN58": "During the past 30 days, what brand of cigars, cigarillos, or little cigars did you usually use?", # REMOVE
    "QN59": "Did any of the flavors that you used in the past 30 days have names or descriptions that included the word “ice” or “iced” (for example, blueberry ice or strawberry ice)?", # REMOVE
    "QN60": "Did any of the flavors that you used in the past 30 days have a name that did not describe a specific flavor, such as “solar,” “purple,” “jazz,” “island bash,” “fusion” or some other word or phrase?", # REMOVE
    "QN62": "Have you ever been curious about smoking a cigar, cigarillo, or little cigar?", # REMOVE
    "QN63": "Do you think you will try a cigar, cigarillo, or little cigar soon?", # REMOVE
    "QN64": "Do you think you will smoke a cigar, cigarillo, or little cigar in the next year?", # REMOVE
    "QN65": "If one of your best friends were to offer you a cigar, cigarillo, or little cigar, would you smoke it?", # REMOVE
    "QN66": "Have you ever smoked part or all of a cigar, cigarillo, or little cigar with marijuana in it?", # REMOVE
    "QN67": "Have you ever used chewing tobacco, snuff, or dip, even just a small amount?", # REMOVE
    "QN68": "How old were you when you first used chewing tobacco, snuff, or dip, even just a small amount", # REMOVE
    "QN69": "During the past 30 days, on how many days did you use chewing tobacco, snuff, or dip?", # REMOVE
    "QN70A": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Copenhagen)", # REMOVE
    "QN70B": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Grizzly)", # REMOVE
    "QN70C": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Kayak)", # REMOVE
    "QN70D": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Kodiak)", # REMOVE
    "QN70E": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Longhorn)", # REMOVE
    "QN70F": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Red Man)", # REMOVE
    "QN70G": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Red Seal)", # REMOVE
    "QN70H": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Skoal)", # REMOVE
    "QN70J": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Timber Wolf)", # REMOVE
    "QN70K": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Some other brand(s) not listed here)", # REMOVE
    "QN70L": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Not sure / I don’t know the brand)", # REMOVE
    "QN71": "During the past 30 days, what brand of chewing tobacco, snuff, or dip did you usually use?", # REMOVE
    "QN72": "How old was this person?", # REMOVE
    "QN73": "Have you ever been curious about using chewing tobacco, snuff, or dip?", # REMOVE
    "QN74": "Have you ever used snus, even just one time?", # REMOVE
    "QN75": "During the past 30 days, on how many days did you use snus?", # REMOVE
    "QN76": "Before today, have you heard of nicotine pouches?", # REMOVE
    "QN77": "Have you ever used a nicotine pouch, even just one time?", # MERGE to NC4: "Respondent has used a nicotine pouch."
    "QN78": "During the past 30 days, on how many days did you use a nicotine pouch?", # REMOVE
    "QN79A": "During the past 30 days, what nicotine pouch brands did you use? (2ONE)", # REMOVE
    "QN79B": "During the past 30 days, what nicotine pouch brands did you use? (FRE)", # REMOVE
    "QN79C": "During the past 30 days, what nicotine pouch brands did you use? (on!)", # REMOVE
    "QN79D": "During the past 30 days, what nicotine pouch brands did you use? (Rogue)", # REMOVE
    "QN79E": "During the past 30 days, what nicotine pouch brands did you use? (VELO)", # REMOVE
    "QN79F": "During the past 30 days, what nicotine pouch brands did you use? (ZYN)", # REMOVE
    "QN79G": "During the past 30 days, what nicotine pouch brands did you use? (Juice Head ZTN)", # REMOVE
    "QN79H": "During the past 30 days, what nicotine pouch brands did you use? (Some other brand(s) not listed here)", # REMOVE
    "QN79I": "During the past 30 days, what nicotine pouch brands did you use? (Not sure / I don’t know the brand", # REMOVE
    "QN80": "During the past 30 days, what brand of nicotine pouches did you usually use?", # REMOVE
    "QN81": "Did any of the flavors that you used in the past 30 days have names or descriptions that included the word “ice” or “iced” (for example, blueberry ice or strawberry ice)?", # MERGE to NC9: "Respondent has bought e-cigarettes or nicotine pouches with flavors that include the word “ice” or “iced”".
    "QN82": "Did any of the flavors that you used in the past 30 days have a name that did not describe a specific flavor, such as “solar,” “purple,” “jazz,” “island bash,” “fusion” or some other word or phrase?", # MERGE to NC10: "Respondent has bought e-cigarettes or nicotine pouches with flavors that included specific flavors".
    "QN83": "Have you ever used any oral nicotine products, even just one time?", # MERGE to NC5: "Respondent used oral nicotine products"
    "QN84": "During the past 30 days, on how many days did you use oral nicotine products?", # REMOVE
    "QN85": "Have you ever smoked tobacco in a hookah or waterpipe, even one or two puffs?", # REMOVE
    "QN86": "How old were you when you first smoked tobacco in a hookah or waterpipe, even one or two puffs?", # REMOVE
    "QN87": "During the past 30 days, on how many days did you smoke tobacco in a hookah or waterpipe?", # REMOVE
    "QN88A": "During the past 30 days, where did you smoke tobacco in a hookah or waterpipe? (At my house)", # REMOVE
    "QN88B": "During the past 30 days, where did you smoke tobacco in a hookah or waterpipe? (At a friend’s house)", # REMOVE
    "QN88C": "During the past 30 days, where did you smoke tobacco in a hookah or waterpipe? (At a family member’s house, other than my house)", # REMOVE
    "QN88D": "During the past 30 days, where did you smoke tobacco in a hookah or waterpipe? (At a hookah bar)", # REMOVE
    "QN88E": "During the past 30 days, where did you smoke tobacco in a hookah or waterpipe? (At a café or restaurant)", # REMOVE
    "QN88F": "During the past 30 days, where did you smoke tobacco in a hookah or waterpipe? (Some other place not listed here)", # REMOVE
    "QN89": "How old was this person?", # REMOVE
    "QN90": "Have you ever been curious about smoking tobacco in a hookah or waterpipe?", # REMOVE
    "QN91": "Before today, have you heard of heated tobacco products", # REMOVE
    "QN92": "Have you ever used a heated tobacco product, even just one time?", # REMOVE
    "QN93": "During the past 30 days, on how many days did you use a heated tobacco product?", # REMOVE
    "QN94": "Have you ever smoked pipes filled with tobacco (not hookah or waterpipe), even just one time?", # REMOVE
    "QN95": "During the past 30 days, on how many days did you smoke pipes filled with tobacco?", # REMOVE
    "QN96": "Have you ever smoked bidis, even just one time?", # REMOVE
    "QN97": "During the past 30 days, on how many days did you smoke bidis?", # REMOVE
    "QN98": "Have you ever smoked roll-your-own cigarettes, even just one time?", # REMOVE
    "QN99": "During the past 30 days, on how many days did you smoke roll-your-own cigarettes?", # REMOVE
    "QN100": "During the past 30 days, on how many days did you use any tobacco product(s)?", # -> CATEGORICAL: 0 or >0 aka "Tobacco User" or "Non-user"
    "QN101": "During the past 30 days, have you had a strong craving or felt like you really needed to use a tobacco product of any kind?", # -> CATEGORICAL: 0 or 1 aka "Tobacco User" or "Non-user"
    "QN102": "How soon after you wake up do you want to use a tobacco product of any kind?", # REMOVE
    "QN103": "Are you seriously thinking about quitting the use of all tobacco products?", # REMOVE
    "QN104": "During the past 12 months, how many times have you stopped using all tobacco products for one day or longer because you were trying to quit all tobacco products for good?", # REMOVE
    "QN105": "During the past 30 days, did anyone refuse to sell you any tobacco products because of your age", # REMOVE
    "QN106": "How easy do you think it is for people your age to buy tobacco products in a store?", # REMOVE
    "QN107": "How easy do you think it is for people your age to buy tobacco products online?", # REMOVE
    "QN108": "During the past 30 days, how often did you see a warning label on… (An e- cigarette package?)", # REMOVE
    "QN109": "During the past 30 days, how often did you see a warning label on… (A cigarette package?)", # REMOVE
    "QN110": "During the past 30 days, how often did you see a warning label on… (A cigar, cigarillo, or little cigar package?)", # REMOVE
    "QN111": "During the past 30 days, how often did you see a warning label on… (A package of chewing tobacco, snuff, or dip?)", # REMOVE
    "QN112": "During the past 30 days, how often did you see a warning label on… (A package of hookah tobacco?)", # REMOVE
    "QN113": "How much do you think people harm themselves when they smoke cigarettes some days but not every day?", # REMOVE
    "QN114": "How much do you think people harm themselves when they smoke cigars, cigarillos, or little cigars, some days but not every day?", # REMOVE
    "QN115": "Do you believe that cigars, cigarillos, or little cigars are (LESS ADDICTIVE, EQUALLY ADDICTIVE, or MORE ADDICTIVE) than cigarettes?", # REMOVE
    "QN116": "How much do you think people harm themselves when they use e-cigarettes some days but not every day?", # REMOVE
    "QN117": "Do you believe that e-cigarettes are (LESS ADDICTIVE, EQUALLY ADDICTIVE, or MORE ADDICTIVE) than cigarettes?", # -> CATEGORICAL: just split into three columns
    "QN118": "Compared to a typical cigarette, would you think that a cigarette advertised as low nicotine would be…", # REMOVE
    "QN119": "Out of every 10 students in your grade at school, how many do you think smoke cigarettes?", # -> CATEGORICAL: 1-3, 4-6, 7-10 (Respondent percieves that not that many people smoke cigarettes, a good amount do, or many do)
    "QN120": "Out of every 10 students in your grade at school, how many do you think use e- cigarettes?", # -> CATEGORICAL: 1-3, 4-6, 7-10 (Respondent percieves that not that many people smoke e-cigarettes, a good amount do, or many do)
    "QN121": "How often do you use social media?", # -> CATEGORICAL: 1-5 (Never-Moderate use) or 6-8 (Frequent use)
    "QN122": "When you use social media, how often do you see posts or content (pictures, videos, or text) related to e-cigarettes?", # -> CATEGORICAL: 1-3 (Never-Moderate social media exposure) or 4-5 (Frequent social media exposure)
    "QN123A": "On which social media sites have you seen posts or content related to e- cigarettes? (Facebook)", # REMOVE 
    "QN123B": "On which social media sites have you seen posts or content related to e- cigarettes? (Instagram)", # REMOVE 
    "QN123C": "On which social media sites have you seen posts or content related to e- cigarettes? (Snapchat)", # REMOVE 
    "QN123D": "On which social media sites have you seen posts or content related to e- cigarettes? (TikTok)", # REMOVE 
    "QN123E": "On which social media sites have you seen posts or content related to e- cigarettes? (Twitch)", # REMOVE 
    "QN123F": "On which social media sites have you seen posts or content related to e- cigarettes? (Twitter)", # REMOVE 
    "QN123G": "On which social media sites have you seen posts or content related to e- cigarettes? (Reddit)", # REMOVE 
    "QN123H": "On which social media sites have you seen posts or content related to e- cigarettes? (YouTube)", # REMOVE 
    "QN123I": "On which social media sites have you seen posts or content related to e- cigarettes? (Some other site)", # REMOVE 
    "QN124": "When you use social media, how often do you post pictures or videos of yourself or someone else using e-cigarettes?", # REMOVE 
    "QN125": "When you use social media, how often have you liked, commented, or shared posts or content (pictures, videos, or text) related to e-cigarettes?", # REMOVE 
    "QN126A": "Who usually posted the content related to e-cigarettes on your social media? (People I know in real life)", # REMOVE 
    "QN126B": "Who usually posted the content related to e-cigarettes on your social media? (Online friends I have not met in real life)", # REMOVE 
    "QN126C": "Who usually posted the content related to e-cigarettes on your social media? (Celebrities or social media influencers)", # REMOVE 
    "QN126D": "Who usually posted the content related to e-cigarettes on your social media? (E-cigarette brands or sellers)", # REMOVE 
    "QN126E": "Who usually posted the content related to e-cigarettes on your social media? (Online news articles)", # REMOVE 
    "QN126G": "Who usually posted the content related to e-cigarettes on your social media? (Other)", # REMOVE 
    "QN127": "During the past 7 days, on how many days did someone smoke tobacco products in your home while you were there?", # -> CATEGORICAL: 0 or >0 aka "Tobacco exposure at home or not"
    "QN128": "During the past 7 days, on how many days did you ride in a vehicle when someone was smoking a tobacco product?", # -> CATEGORICAL: 0 or >0 aka "Tobacco exposure in vehicles or not"
    "QN129": "During the past 30 days, on how many days were you exposed to the smoke from someone who was smoking tobacco products in an indoor public place?", # REMOVE
    "QN130": "During the past 30 days, on how many days were you exposed to the smoke from someone who was smoking tobacco products in an outdoor public place?", # REMOVE
    "QN131": "During the past 7 days, on how many days did someone use e-cigarettes in your home while you were there?",  # -> CATEGORICAL: 0 or >0 aka "e-cig exposure at home or not"
    "QN132": "During the past 7 days, on how many days did you ride in a vehicle when someone was using an e-cigarette?", # -> CATEGORICAL: 0 or >0 aka "e-cig exposure in vehicles or not"
    "QN133": "During the past 30 days, on how many days were you exposed to the vapor from someone who was using an e-cigarette in an indoor public place?", # REMOVE
    "QN134": "During the past 30 days, on how many days were you exposed to the vapor from someone who was using an e-cigarette in an outdoor public place?", # REMOVE
    "QN135A": "While at school or on school property, have you ever seen anyone using an e- cigarette, such as JUUL, Vuse, NJOY, Elf Bar, or blu in any of the following locations? (Yes, inside a school bathroom or locker room)", # MERGE to NC11: "Respondent has witnessed e-cigarette use at school"
    "QN135B": "While at school or on school property, have you ever seen anyone using an e- cigarette, such as JUUL, Vuse, NJOY, Elf Bar, or blu in any of the following locations? (Yes, inside a classroom)", # MERGE to NC11: "Respondent has witnessed e-cigarette use at school"
    "QN135C": "While at school or on school property, have you ever seen anyone using an e- cigarette, such as JUUL, Vuse, NJOY, Elf Bar, or blu in any of the following locations? (Yes, inside some other area of the school (hallway, cafeteria)", # MERGE to NC11: "Respondent has witnessed e-cigarette use at school"
    "QN135D": "While at school or on school property, have you ever seen anyone using an e- cigarette, such as JUUL, Vuse, NJOY, Elf Bar, or blu in any of the following locations? (Yes, outside of the school)", # MERGE to NC11: "Respondent has witnessed e-cigarette use at school"
    "QN135E": "While at school or on school property, have you ever seen anyone using an e- cigarette, such as JUUL, Vuse, NJOY, Elf Bar, or blu in any of the following locations? (Yes, somewhere else not listed here", # MERGE to NC11: "Respondent has witnessed e-cigarette use at school"
    "QN135F": "While at school or on school property, have you ever seen anyone using an e- cigarette, such as JUUL, Vuse, NJOY, Elf Bar, or blu in any of the following locations? (No)", # REMOVE
    "QN136A": "Does anyone who lives with you now…? (Use e-cigarettes)", 
    "QN136B": "Does anyone who lives with you now…? (Smoke cigarettes)", # MERGE to NC12: "Respondent lives with someone who uses Tobacco products"
    "QN136C": "Does anyone who lives with you now…? (Smoke cigars, cigarillos, or little cigars)", # MERGE to NC12: "Respondent lives with someone who uses Tobacco products"
    "QN136D": "Does anyone who lives with you now…? (Use chewing tobacco, snuff, or dip)", # MERGE to NC12: "Respondent lives with someone who uses Tobacco products"
    "QN136E": "Does anyone who lives with you now…? (Use snus)", # MERGE to NC12: "Respondent lives with someone who uses Tobacco products"
    "QN136F": "Does anyone who lives with you now…? (Use nicotine pouches)",
    "QN136G": "Does anyone who lives with you now…? (Use other oral nicotine products)",
    "QN136H": "Does anyone who lives with you now…? (Smoke tobacco in a hookah or waterpipe)", # MERGE to NC12: "Respondent lives with someone who uses Tobacco products"
    "QN136I": "Does anyone who lives with you now…? (Use heated tobacco products)", # MERGE to NC12: "Respondent lives with someone who uses Tobacco products"
    "QN136J": "Does anyone who lives with you now…? (Smoke pipes filled with tobacco (not hookah or waterpipe))", # MERGE to NC12: "Respondent lives with someone who uses Tobacco products"
    "QN136K": "Does anyone who lives with you now…? (Smoke bidis)", # MERGE to NC12: "Respondent lives with someone who uses Tobacco products"
    "QN136L": "Does anyone who lives with you now…? (Smoke roll-your-own cigarettes)", # MERGE to NC12: "Respondent lives with someone who uses Tobacco products"
    "QN136M": "Does anyone who lives with you now…? (No one who lives with me now uses any form of tobacco)", # REMOVE
    "QN137A": "Have you experienced this? (You were discouraged from joining an advanced level class)", # MERGE to NC13: "Respodent has experience psychological distress or discrimination"
    "QN137B": "Have you experienced this? (You were wrongly disciplined or given after-school detention)", # MERGE to NC13: "Respodent has experience psychological distress or discrimination"
    "QN137C": "Have you experienced this? (You were given a lower grade than you deserved)", # MERGE to NC13: "Respodent has experience psychological distress or discrimination related to school"
    "QN137D": "Have you experienced this? (You were discouraged from joining a club)", # MERGE to NC13: "Respodent has experience psychological distress or discrimination related to school"
    "QN137E": "Have you experienced this? (Others your age did not include you in their activities)", # MERGE to NC13: "Respodent has experience psychological distress or discrimination related to school"
    "QN137F": "Have you experienced this? (People expected more of you than they expected of others your age)", # REMOVE
    "QN137G": "Have you experienced this? (People expected less of you than they expected of others your age)", # REMOVE
    "QN137H": "Have you experienced this? (People assumed your English was poor)", # MERGE to NC14: "Respodent has experience discrimination (general)"
    "QN137I": "Have you experienced this? (You were hassled by the police)", # MERGE to NC14: "Respodent has experience discrimination (general)"
    "QN137J": "Have you experienced this? (You were hassled by a store clerk or store guard)", # MERGE to NC14: "Respodent has experience discrimination (general)"
    "QN137K": "Have you experienced this? (You were called racially insulting names)", # MERGE to NC14: "Respodent has experience discrimination (general)"
    "QN137L": "Have you experienced this? (You received poor service at a restaurant or store)", # MERGE to NC14: "Respodent has experience discrimination (general)"
    "QN137M": "Have you experienced this? (People acted as if they thought you were not smart)", # MERGE to NC14: "Respodent has experience discrimination (general)"
    "QN137N": "Have you experienced this? (People acted as if they were afraid of you)", # MERGE to NC14: "Respodent has experience discrimination (general)"
    "QN137O": "Have you experienced this? (You were threatened)", # REMOVE
    "QN138A": "How much did this experience upset you? (You were discouraged from joining an advanced level class)", # REMOVE but Notes on the following: the NC13-14 can be improved by combining it with the following columns if their upset level is high
    "QN138B": "How much did this experience upset you? (You were wrongly disciplined or given after-school detention)", # REMOVE
    "QN138C": "How much did this experience upset you? (You were given a lower grade than you deserved)", # REMOVE
    "QN138D": "How much did this experience upset you? (You were discouraged from joining a club)", # REMOVE
    "QN138E": "How much did this experience upset you? (Others your age did not include you in their activities)", # REMOVE
    "QN138F": "How much did this experience upset you? (People expected more of you than they expected of others your age)", # REMOVE
    "QN138G": "How much did this experience upset you? (People expected less of you than they expected of others your age)", # REMOVE
    "QN138H": "How much did this experience upset you? (People assumed your English was poor)", # REMOVE
    "QN138I": "How much did this experience upset you? (You were hassled by the police)", # REMOVE
    "QN138J": "How much did this experience upset you? (You were hassled by a store clerk or store guard)", # REMOVE
    "QN138K": "How much did this experience upset you? (You were called racially insulting names)", # REMOVE
    "QN138L": "How much did this experience upset you? (You received poor service at a restaurant or store)", # REMOVE
    "QN138M": "How much did this experience upset you? (People acted as if they thought you were not smart)", # REMOVE
    "QN138N": "How much did this experience upset you? (People acted as if they were afraid of you)", # REMOVE
    "QN138O": "How much did this experience upset you? (You were threatened)", # REMOVE
    "QN139A": "How true are the following statements about your neighborhood? (There are plenty of safe places to walk or spend time outdoors in my neighborhood)",  # CATEGORICAL: 1-2 (Unsafe Neighborhood) or 3-4 (Safe Neighborhood)
    "QN139B": "How true are the following statements about your neighborhood? (Every few weeks, some kid in my neighborhood gets beat-up or mugged)", # CATEGORICAL: 1-2 (Safe Neighborhood) or 3-4 (Unsafe Neighborhood)
    "QN139C": "How true are the following statements about your neighborhood? (Every few weeks, some adult gets beat-up or mugged in my neighborhood)", # CATEGORICAL: 1-2 (Safe Neighborhood) or 3-4 (Unsafe Neighborhood)
    "QN139D": "How true are the following statements about your neighborhood? (I have seen people using or selling drugs in my neighborhood)", # CATEGORICAL: 1-2 (Unsafe Neighborhood) or 3-4 (Safe Neighborhood)
    "QN139E": "How true are the following statements about your neighborhood? (In the morning or later in the day, I often see drunk people on the street in my neighborhood)", # REMOVE
    "QN139F": "How true are the following statements about your neighborhood? (Most adults in my neighborhood respect the law)", # REMOVE
    "QN139G": "How true are the following statements about your neighborhood? (I feel safe when I walk around my neighborhood by myself during the day)", # CATEGORICAL: 1-2 (Unsafe Neighborhood) or 3-4 (Safe Neighborhood)
    "QN139H": "How true are the following statements about your neighborhood? (People who live in my neighborhood often damage or steal each other’s property)", # CATEGORICAL: 3-4 (Unsafe Neighborhood) or 1-2 (Safe Neighborhood)
    "QN139I": "How true are the following statements about your neighborhood? (I feel safe when I walk around my neighborhood by myself at night)", # CATEGORICAL: 1-2 (Unsafe Neighborhood) or 3-4 (Safe Neighborhood)
    "QN139J": "How true are the following statements about your neighborhood? (In my neighborhood, the people with the most money are the drug dealers)", # CATEGORICAL: 3-4 (Unsafe Neighborhood) or 1-2 (Safe Neighborhood)
    "QN140": "Do you speak a language other than English at home?",
    "QN141": "Which of these options best describes your sexual orientation", # REMOVE
    "QN142": "Which of the following best describes your gender?", # REMOVE
    "QN143": "Are you transgender?",
    "QN144": "During the past two weeks, how often have you been bothered by any of the following problems? (Little interest or pleasure in doing things)", # CATEGORICAL: 1 (Good mental state) or >1 Moderate to severe mental distress"
    "QN145": "During the past two weeks, how often have you been bothered by any of the following problems? (Feeling down, depressed, or hopeless)", # CATEGORICAL: 1 (Good mental state) or >1 Moderate to severe mental distress"
    "QN146": "During the past two weeks, how often have you been bothered by any of the following problems? (Feeling nervous, anxious, or on edge)", # CATEGORICAL: 1 (Good mental state) or >1 Moderate to severe mental distress"
    "QN147": "During the past two weeks, how often have you been bothered by any of the following problems? (Not being able to stop or control worrying)", # CATEGORICAL: 1 (Good mental state) or >1 Moderate to severe mental distress"
    "QN148": "During the past 12 months, how would you describe your grades in school?", # Tricky one
    "QN149": "Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions?", # CATEGORICAL: 0 (Good mental state) or 1 Moderate to severe mental distress"
    "Q11n_TEXT": "Why did you first use an e-cigarette? (Specify)", # From this point on, all TEXT columns will be DROPPED manually
    "Q12n_TEXT": "Why do you currently use e-cigarettes? (Specify)", #
    "Q14o_TEXT": "During the past 30 days, what e-cigarette brands did you use? (Specify)", #
    "Q18a_k_TEXT": "In the past 30 days when you used e-cigarettes, what flavors did you use? (Specify)", #
    "Q18b_j_TEXT": "In the past 30 days when you used cigars, cigarillos, or little cigars, what flavors did you use? (Specify)", #
    "Q18c_j_TEXT": "In the past 30 days when you used smokeless tobacco, what flavors did you use? (Specify)", #
    "Q18d_j_TEXT": "In the past 30 days when you used snus, what flavors did you use? (Specify", #
    "Q18e_k_TEXT": "In the past 30 days that you used nicotine pouches, what flavors did you use? (Specify)", #
    "Q18f_k_TEXT": "In the past 30 days when you used oral nicotine products, what flavors did you use? (Specify)", #
    "Q18g_j_TEXT": "In the past 30 days when you used hookah or waterpipe, what flavors did you use? (Specify)", #
    "Q18h_k_TEXT": "In the past 30 days when you used heated tobacco products, what flavors did you use? (Specify)", #
    "Q18i_j_TEXT": "In the past 30 days when you smoked pipes filled with tobacco, what flavors did you use? (Specify)", #
    "Q18j_j_TEXT": "In the past 30 days when you used bidis, what flavors did you use? (Specify", #
    "Q18k_j_TEXT": "In the past 30 days when you used roll-your-own cigarettes, what flavors did you use? (Specify)", #
    "Q20_TEXT": "Did any of the flavors that you used in the past 30 days have a name that did not describe a specific flavor, such as “solar,” “purple,” “jazz,” “island bash,” “fusion” or some other word or phrase? (Specify)", #
    "Q21a_h_TEXT": "During the past 30 days, how did you get your e-cigarette devices, pods, cartridges, or e-liquid refills? (Specify)", #
    "Q21b_h_TEXT": "During the past 30 days, how did you get your cigarettes? (Specify)", #
    "Q21c_h_TEXT": "During the past 30 days, how did you get your cigars, cigarillos, or little cigars? (Specify)", #
    "Q21d_h_TEXT": "During the past 30 days, how did you get your chewing tobacco, snuff, or dip? (Specify)", #
    "Q21e_h_TEXT": "During the past 30 days, how did you get your snus? (Specify)", #
    "Q21f_h_TEXT": "During the past 30 days, how did you get your nicotine pouches? (Specify)", #
    "Q21g_h_TEXT": "During the past 30 days, how did you get your oral nicotine products? (Specify", #
    "Q21h_h_TEXT": "During the past 30 days, how did you get your hookah tobacco? (Specify", #
    "Q21i_h_TEXT": "During the past 30 days, how did you get your heated tobacco products? (Specify", #
    "Q21j_h_TEXT": "During the past 30 days, how did you get your pipe tobacco? (Specify)", #
    "Q21k_h_TEXT": "During the past 30 days, how did you get your bidis? (Specify)", #
    "Q21l_h_TEXT": "During the past 30 days, how did you get your roll-your-own cigarettes? (Specify", #
    "Q22a_l_TEXT": "During the past 30 days, where did you buy your e-cigarette devices, pods, cartridges, or e-liquid refills? (Specify)", #
    "Q22b_l_TEXT": "During the past 30 days, where did you buy your cigarettes? (Specify)", #
    "Q22c_l_TEXT": "During the past 30 days, where did you buy your cigars, cigarillos, or little cigars? (Specify)", #
    "Q22d_l_TEXT": "During the past 30 days, where did you buy your chewing tobacco, snuff, or dip? (Specify)", #
    "Q22e_l_TEXT": "During the past 30 days, where did you buy your snus? (Specify)", #
    "Q22f_l_TEXT": "During the past 30 days, where did you buy your nicotine pouches? (Specify", #
    "Q22g_l_TEXT": "During the past 30 days, where did you buy your oral nicotine products? (Specify", #
    "Q22h_l_TEXT": "During the past 30 days, where did you buy your hookah tobacco? (Specify", #
    "Q22i_l_TEXT": "During the past 30 days, where did you buy your heated tobacco products? (Specify", #
    "Q22j_l_TEXT": "During the past 30 days, where did you buy your pipe tobacco? (Specify)", #
    "Q22k_l_TEXT": "During the past 30 days, where did you buy your bidis? (Specify)", #
    "Q22l_l_TEXT": "During the past 30 days, where did you buy your roll-your-own cigarettes? (Specify", #
    "Q24d_TEXT": "During the past 30 days, which of the following e-cigarette product(s) did you get or buy from another person? (Specify", #
    "Q29j_TEXT": "When you tried to quit using e-cigarettes, did you use any of the following? (Specify", #
    "Q34d_TEXT": "Have you ever vaped any of the following substances (even once)? (Specify", #
    "Q42l_TEXT": "During the past 30 days, what brands of cigarettes did you smoke? (Specify)", #
    "Q57m_TEXT": "During the past 30 days, what brands of cigars, cigarillos, or little cigars did you smoke? (Specify)", #
    "Q60_TEXT": "Did any of the flavors that you used in the past 30 days have a name that did not describe a specific flavor, such as “solar,” “purple,” “jazz,” “island bash,” “fusion” or some other word or phrase?", #
    "Q70k_TEXT": "During the past 30 days, what brands of chewing tobacco, snuff, or dip did you use? (Specify)", #
    "Q79h_TEXT": "During the past 30 days, what nicotine pouch brands did you use? (Specify)", #
    "Q82_TEXT": "Did any of the flavors that you used in the past 30 days have a name that did not describe a specific flavor, such as “solar,” “purple,” “jazz,” “island bash,” “fusion” or some other word or phrase? (Specify)", #
    "Q123i_TEXT": "On which social media sites have you seen posts or content related to e- cigarettes? (Specify)", #
    "Q126g_TEXT": "Who usually posted the content related to e-cigarettes on your social media? (Specify)", #
    "Q135e_TEXT": "While at school or on school property, have you ever seen anyone using an e-cigarette, such as JUUL, Vuse, NJOY, Elf Bar, or blu in any of the following locations? (Specify)", #
    "Q141_TEXT": "Which of these options best describes your sexual orientation? (Specify)", #
    "Q142_TEXT": "Which of the following best describes your gender? (Specify)", #
    "AGEGRP": "The percentage of all students who reported their age to be < 18 years of age",
    "SEX": "The percentage of all students who reported being either female or male",
    "SCHOOLTYPE": "The percentage of all students who reported being in 6th, 7th, or 8th grade (middle school), or in 9th, 10th, 11th, or 12th grade (high school)",
    "MRACE": "Number of races chosen from Q5",
    "RACE_M": "Race/Eth - mult grp",
    "RACE_S": "Race/Eth - no mult grp",
    "SEXID": "The percentage of all students who reported being best described as straight/heterosexual, or gay/lesbian, or bisexual/pansexual/queer/asexual, or I not sure/questioning, or I do not know what this question means",
    "SEXID2": "The percentage of all students who reported being best described as straight/heterosexual, or gay/lesbian/bisexual/pansexual/queer/asexual, or I am not sure/questioning, or I do not know what this question means",
    "EBIDIS": "The percentage of all students who reported they have ever tried bidis (small brown cigarettes wrapped in a leaf)",
    "PSU": "Primary Sampling Unit",
    "PSU_NUM": "Primary Sampling Unit (Numeric)",
    "Stratum": "Stratum for Variance",
    "Stratum_num": "Stratum for Variance",
    "WT_Analysis": "Final Weight",
}
