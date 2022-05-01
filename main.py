# William Tucker
# The purpose of this program is to evaluate NFL draft prospects and determine
# whether they are worth a first round draft pick based on their college stats
# and combine results.
# Last updated 4/30/2022

# This function uses stats that I feel are reflective of a good quarterback
# prospect and place value according to what stats I believe are most
# important. Feel free to change any of the numbers to reflect your view of
# what a good QB is.
def quarterback_evaluation():
    global qb_passing_yards, qb_completion_percentage, qb_passing_touchdowns, \
        qb_interceptions
    successful_qb_passing_yards = False
    successful_qb_completion_percentage = False
    successful_qb_passing_touchdowns = False
    successful_qb_interceptions = False
    while not successful_qb_passing_yards:
        try:
            qb_passing_yards = int(
                input("How many yards did he pass for last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_qb_passing_yards = True
    while not successful_qb_completion_percentage:
        try:
            qb_completion_percentage = float(
                input("What was his completion percentage last season? "
                      "(Please omit the \"%\"): "))
        except:
            print("That was not a valid entry.")
        else:
            successful_qb_completion_percentage = True
    while not successful_qb_passing_touchdowns:
        try:
            qb_passing_touchdowns = int(
                input("How many touchdowns did he throw for last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_qb_passing_touchdowns = True
    while not successful_qb_interceptions:
        try:
            qb_interceptions = int(input(
                "How many interceptions did he throw for last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_qb_interceptions = True
    total_qb_score = round(
        ((qb_passing_yards / 100) + qb_completion_percentage) * \
        ((qb_passing_touchdowns - qb_interceptions) / 10))
    if total_qb_score >= 200:
        print(
            "This quarterback is worth a first round draft pick. His overall "
            "grade is", total_qb_score)
    else:
        print(
            "This quarterback is not worth a first round draft pick. His "
            "overall grade is", total_qb_score)


# This function prints my opinion that running backs are not worth first round
# picks. If you disagree, feel free to write code here to determine what a
# first round RB is in your opinion. If you need to, reference the structure I
# use when evaluating other positions.
def running_back_evaluation():
    print("A running back is not worth a first round draft pick.")


# This function uses stats that I feel are reflective of a good wide receiver
# prospect and place value according to what stats I believe are most
# important. Feel free to change any of the numbers to reflect your view of
# what a good WR is.
def wide_receiver_evaluation():
    global wr_receiving_yards, wr_receptions, wr_receiving_touchdowns, \
        wr_40_time, wr_vertical
    successful_wr_receiving_yards = False
    successful_wr_receptions = False
    successful_wr_receiving_touchdowns = False
    successful_wr_40 = False
    successful_wr_vertical = False
    while not successful_wr_receiving_yards:
        try:
            wr_receiving_yards = int(
                input("How many receiving yards did he have last year?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_wr_receiving_yards = True
    while not successful_wr_receptions:
        try:
            wr_receptions = int(
                input("How many receptions did he have last year?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_wr_receptions = True
    while not successful_wr_receiving_touchdowns:
        try:
            wr_receiving_touchdowns = int(input(
                "How many receiving touchdowns did he have last year?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_wr_receiving_touchdowns = True
    while not successful_wr_40:
        try:
            wr_40_time = float(input("What is his 40 yard dash time?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_wr_40 = True
    while not successful_wr_vertical:
        try:
            wr_vertical = float(
                input("What is his vertical leap in inches?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_wr_vertical = True
    total_wr_score = round(
        (wr_receiving_yards / wr_receptions) * wr_receiving_touchdowns)
    if wr_40_time <= 4.5 and wr_vertical >= 37:
        ideal_wr_combine = True
    else:
        ideal_wr_combine = False
    if total_wr_score >= 200 and ideal_wr_combine:
        print(
            "This wide receiver is worth a first round draft pick. His overall"
            " grade is", total_wr_score)
    else:
        print(
            "This wide receiver is not worth a first round draft pick. His "
            "overall grade is", total_wr_score)


# This function prints my opinion that tight ends are not worth first round
# picks. If you disagree, feel free to write code here to determine what a
# first round TE is in your opinion. If you need to, reference the structure I
# use when evaluating other positions.
def tight_end_evaluation():
    print("A tight end is not worth a first round draft pick.")


# This function uses stats that I feel are reflective of a good offensive
# tackle prospect and place value according to what stats I believe are most
# important. Feel free to change any of the numbers to reflect your view of
# what a good OT is.
def offensive_tackle_evaluation():
    global ot_height, ot_weight, ot_bench_press, ot_shuttle, ot_penalties
    successful_ot_height = False
    successful_ot_weight = False
    successful_ot_bench_press = False
    successful_ot_shuttle = False
    successful_ot_penalties = False
    while not successful_ot_height:
        try:
            ot_height = int(input("Please enter his height in inches: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_ot_height = True
    while not successful_ot_weight:
        try:
            ot_weight = int(input("Please enter his weight in pounds: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_ot_weight = True
    while not successful_ot_bench_press:
        try:
            ot_bench_press = int(
                input("How many reps does he bench at 225 pounds?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_ot_bench_press = True
    while not successful_ot_shuttle:
        try:
            ot_shuttle = float(input("What is his shuttle drill time?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_ot_shuttle = True
    while not successful_ot_penalties:
        try:
            ot_penalties = int(
                input("How many penalties did he commit last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_ot_penalties = True
    if ot_height >= 77 and ot_weight >= 320:
        ot_ideal_measurables = True
    else:
        ot_ideal_measurables = False
    if ot_bench_press >= 23 and ot_shuttle <= 4.7:
        ot_ideal_combine = True
    else:
        ot_ideal_combine = False
    if ot_ideal_measurables and ot_ideal_combine and ot_penalties <= 8:
        print("This offensive tackle is worth a first round pick.")
    else:
        print("This offensive tackle is not worth a first round pick.")


# This function uses stats that I feel are reflective of a good interior
# offensive lineman prospect and place value according to what stats I believe
# are most important. Feel free to change any of the numbers to reflect your
# view of what a good IOL is.
def interior_offensive_lineman_evaluation():
    global iol_height, iol_weight, iol_bench_press, iol_penalties
    successful_iol_height = False
    successful_iol_weight = False
    successful_iol_bench_press = False
    successful_iol_penalties = False
    while not successful_iol_height:
        try:
            iol_height = int(input("Please enter his height in inches: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_iol_height = True
    while not successful_iol_weight:
        try:
            iol_weight = int(input("Please enter his weight in pounds: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_iol_weight = True
    while not successful_iol_bench_press:
        try:
            iol_bench_press = int(
                input("How many reps does he bench at 225 pounds?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_iol_bench_press = True
    while not successful_iol_penalties:
        try:
            iol_penalties = int(
                input("How many penalties did he commit last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_iol_penalties = True
    if iol_height >= 75 and iol_weight >= 300:
        iol_ideal_measurables = True
    else:
        iol_ideal_measurables = False
    if iol_ideal_measurables and iol_bench_press >= 30 and iol_penalties <= 8:
        print("This interior offensive lineman is worth a first round pick.")
    else:
        print(
            "This interior offensive lineman is not worth a first round pick.")


# This function uses stats that I feel are reflective of a good edge rusher
# prospect and place value according to what stats I believe are most
# important. Feel free to change any of the numbers to reflect your view of
# what a good EDGE is.
def edge_rusher_evaluation():
    global edge_sacks, edge_tackle_for_loss, edge_height, edge_weight, \
        edge_bench, edge_40_time
    successful_edge_sacks = False
    successful_edge_loss = False
    successful_edge_height = False
    successful_edge_weight = False
    successful_edge_bench_press = False
    successful_edge_40 = False
    while not successful_edge_sacks:
        try:
            edge_sacks = float(
                input("How many sacks did he have last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_edge_sacks = True
    while not successful_edge_loss:
        try:
            edge_tackle_for_loss = float(
                input("How many tackles for loss did he have last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_edge_loss = True
    while not successful_edge_height:
        try:
            edge_height = int(input("Please enter his height in inches: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_edge_height = True
    while not successful_edge_weight:
        try:
            edge_weight = int(input("Please enter his weight in pounds: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_edge_weight = True
    while not successful_edge_bench_press:
        try:
            edge_bench = int(
                input("How many reps does he bench at 225 pounds?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_edge_bench_press = True
    while not successful_edge_40:
        try:
            edge_40_time = float(input("What is his 40 yard dash time?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_edge_40 = True
    edge_score = (edge_sacks * edge_tackle_for_loss) * 2
    if edge_height >= 75 and edge_weight >= 245:
        ideal_edge_measurables = True
    else:
        ideal_edge_measurables = False
    if edge_bench >= 20 and edge_40_time <= 4.8:
        ideal_edge_combine = True
    else:
        ideal_edge_combine = False
    if edge_score >= 150 and ideal_edge_measurables and ideal_edge_combine:
        print(
            "This EDGE rusher is worth a first round draft pick. His overall "
            "grade is", edge_score)
    else:
        print(
            "This EDGE rusher is not worth a first round draft pick. His "
            "overall grade is", edge_score)


# This function uses stats that I feel are reflective of a good defensive
# lineman prospect and place value according to what stats I believe are most
# important. Feel free to change any of the numbers to reflect your view of
# what a good DL is.
def defensive_lineman_evaluation():
    global dl_sacks, dl_tackle_for_loss, dl_height, dl_weight, dl_bench
    successful_dl_sacks = False
    successful_dl_loss = False
    successful_dl_height = False
    successful_dl_weight = False
    successful_dl_bench_press = False
    while not successful_dl_sacks:
        try:
            dl_sacks = float(
                input("How many sacks did he have last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_dl_sacks = True
    while not successful_dl_loss:
        try:
            dl_tackle_for_loss = float(
                input("How many tackles for loss did he have last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_dl_loss = True
    while not successful_dl_height:
        try:
            dl_height = int(input("Please enter his height in inches: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_dl_height = True
    while not successful_dl_weight:
        try:
            dl_weight = int(input("Please enter his weight in pounds: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_dl_weight = True
    while not successful_dl_bench_press:
        try:
            dl_bench = int(
                input("How many reps does he bench at 225 pounds?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_dl_bench_press = True
    dl_score = (dl_sacks * dl_tackle_for_loss) * 2
    if dl_height >= 77 and dl_weight >= 300:
        ideal_dl_measurables = True
    else:
        ideal_dl_measurables = False
    if dl_score >= 150 and dl_bench >= 30 and ideal_dl_measurables:
        print(
            "This defensive lineman is worth a first round draft pick. His "
            "overall grade is", dl_score)
    else:
        print(
            "This defensive lineman is not worth a first round draft pick. His"
            " overall grade is", dl_score)


# This function uses stats that I feel are reflective of a good linebacker
# prospect and place value according to what stats I believe are most
# important. Feel free to change any of the numbers to reflect your view of
# what a good LB is.
def linebacker_evaluation():
    global lb_tackles, lb_tackle_for_loss, lb_height, lb_weight, lb_bench, \
        lb_40_time
    successful_lb_tackles = False
    successful_lb_loss = False
    successful_lb_height = False
    successful_lb_weight = False
    successful_lb_bench_press = False
    successful_lb_40 = False
    while not successful_lb_tackles:
        try:
            lb_tackles = float(
                input("How many tackles did he have last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_lb_tackles = True
    while not successful_lb_loss:
        try:
            lb_tackle_for_loss = float(
                input("How many tackles for loss did he have last season?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_lb_loss = True
    while not successful_lb_height:
        try:
            lb_height = int(input("Please enter his height in inches: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_lb_height = True
    while not successful_lb_weight:
        try:
            lb_weight = int(input("Please enter his weight in pounds: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_lb_weight = True
    while not successful_lb_bench_press:
        try:
            lb_bench = int(
                input("How many reps does he bench at 225 pounds?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_lb_bench_press = True
    while not successful_lb_40:
        try:
            lb_40_time = float(input("What is his 40 yard dash time?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_lb_40 = True
    lb_score = lb_tackles + (lb_tackle_for_loss * 2.5)
    if lb_height >= 72 and lb_weight >= 230:
        lb_ideal_measurables = True
    else:
        lb_ideal_measurables = False
    if lb_bench >= 20 and lb_40_time <= 4.6:
        lb_ideal_combine = True
    else:
        lb_ideal_combine = False
    if lb_score >= 150 and lb_ideal_measurables and lb_ideal_combine:
        print(
            "This linebacker is worth a first round draft pick. His overall "
            "grade is", lb_score)
    else:
        print(
            "This linebacker is not worth a first round draft pick. His "
            "overall grade is", lb_score)


# This function uses stats that I feel are reflective of a good cornerback
# prospect and place value according to what stats I believe are most
# important. Feel free to change any of the numbers to reflect your view of
# what a good CB is.
def cornerback_evaluation():
    global cb_interceptions, cb_pass_deflections, cb_40_time, cb_vertical, \
        cb_height
    successful_cb_interceptions = False
    successful_cb_pass_deflections = False
    successful_cb_height = False
    successful_cb_40 = False
    successful_cb_vertical = False
    while not successful_cb_interceptions:
        try:
            cb_interceptions = int(input(
                "How many total interceptions did he have in college?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_cb_interceptions = True
    while not successful_cb_pass_deflections:
        try:
            cb_pass_deflections = int(input(
                "How many total pass deflections did he have in college?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_cb_pass_deflections = True
    while not successful_cb_height:
        try:
            cb_height = int(input("What is his height in inches?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_cb_height = True
    while not successful_cb_40:
        try:
            cb_40_time = float(input("What is his 40 yard dash time?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_cb_40 = True
    while not successful_cb_vertical:
        try:
            cb_vertical = float(input("What is his vertical in inches?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_cb_vertical = True
    cb_score = (cb_interceptions + cb_pass_deflections) * 7
    if cb_40_time <= 4.5 and cb_vertical >= 35:
        cb_ideal_combine = True
    else:
        cb_ideal_combine = False
    if cb_score >= 150 and cb_height >= 72 and cb_ideal_combine:
        print(
            "This cornerback is worth a first round draft pick. His overall "
            "grade is", cb_score)
    else:
        print(
            "This cornerback is not worth a first round draft pick. His "
            "overall grade is", cb_score)


# This function uses stats that I feel are reflective of a good safety prospect
# and place value according to what stats I believe are most important.
# Feel free to change any of the numbers to reflect your view of what a good S
# is.
def safety_evaluation():
    global s_interceptions, s_pass_deflections, s_40_time, s_vertical, s_height
    successful_s_interceptions = False
    successful_s_pass_deflections = False
    successful_s_height = False
    successful_s_40 = False
    successful_s_vertical = False
    while not successful_s_interceptions:
        try:
            s_interceptions = int(input(
                "How many total interceptions did he have in college?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_s_interceptions = True
    while not successful_s_pass_deflections:
        try:
            s_pass_deflections = int(input(
                "How many total pass deflections did he have in college?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_s_pass_deflections = True
    while not successful_s_height:
        try:
            s_height = int(input("What is his height in inches?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_s_height = True
    while not successful_s_40:
        try:
            s_40_time = float(input("What is his 40 yard dash time?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_s_40 = True
    while not successful_s_vertical:
        try:
            s_vertical = float(input("What is his vertical in inches?: "))
        except:
            print("That was not a valid entry.")
        else:
            successful_s_vertical = True
    s_score = (s_interceptions + s_pass_deflections) * 10
    if s_40_time <= 4.5 and s_vertical >= 35:
        s_ideal_combine = True
    else:
        s_ideal_combine = False
    if s_score >= 150 and s_height >= 72 and s_ideal_combine:
        print(
            "This safety is worth a first round draft pick. His overall grade "
            "is", s_score)
    else:
        print(
            "This safety is not worth a first round draft pick. His overall"
            " grade is", s_score)


# This function allows the user to choose which offensive position to evaluate.
def user_choice_offense():
    quarterback_list = ["qb", "quarterback", "quarter back"]
    running_back_list = ["rb", "runningback", "running back", "hb", "halfback",
                         "half back", "fb", "fullback",
                         "full back"]
    wide_receiver_list = ["wr", "wide receiver", "receiver", "slot",
                          "slot receiver"]
    tight_end_list = ["te", "tight end"]
    offensive_tackle_list = ["ot", "offensive tackle", "lt", "left tackle",
                             "rt", "right tackle"]
    interior_offensive_lineman_list = ["iol", "interior offensive lineman",
                                       "ol", "offensive lineman",
                                       "offensive line", "c", "center", "og",
                                       "offensive guard", "guard",
                                       "lg", "left guard", "rg", "right guard"]
    user_input_offense = input(
        "Please enter the position you want to evaluate: ")
    if user_input_offense.lower() in quarterback_list:
        quarterback_evaluation()
    elif user_input_offense.lower() in running_back_list:
        running_back_evaluation()
    elif user_input_offense.lower() in wide_receiver_list:
        wide_receiver_evaluation()
    elif user_input_offense.lower() in tight_end_list:
        tight_end_evaluation()
    elif user_input_offense.lower() in offensive_tackle_list:
        offensive_tackle_evaluation()
    elif user_input_offense.lower() in interior_offensive_lineman_list:
        interior_offensive_lineman_evaluation()
    else:
        print("That was not a valid entry.")


# This function allows the user to choose which defensive position to evaluate.
def user_choice_defense():
    edge_list = ["edge", "edge rusher", "de", "defensive end",
                 "left defensive end", "left end", "le",
                 "right defensive end", "right end", "re", "pass rusher"]
    dl_list = ["defensive lineman", "dl", "defensive tackle", "dt",
               "nose tackle", "nt"]
    linebacker_list = ["linebacker", "lb", "inside linebacker", "ilb",
                       "middle linebacker", "mlb",
                       "outside linebacker", "olb", "right linebacker",
                       "right outside linebacker", "rolb",
                       "left linebacker", "left outside linebacker", "lolb"]
    cornerback_list = ["cornerback", "corner back", "corner", "cb",
                       "left corner", "left cornerback",
                       "left corner back", "lcb", "right corner",
                       "right cornerback", "right corner back", "rcb",
                       "slot cornerback", "slot corner back"]
    safety_list = ["safety", "s", "free safety", "fs", "strong safety", "ss",
                   "defensive back", "db"]
    user_input_defense = input(
        "Please enter the position you want to evaluate: ")
    if user_input_defense.lower() in edge_list:
        edge_rusher_evaluation()
    elif user_input_defense.lower() in dl_list:
        defensive_lineman_evaluation()
    elif user_input_defense.lower() in linebacker_list:
        linebacker_evaluation()
    elif user_input_defense.lower() in cornerback_list:
        cornerback_evaluation()
    elif user_input_defense.lower() in safety_list:
        safety_evaluation()
    else:
        print("That was not a valid entry.")


# This function prints the order of the draft as of 3/25/2022. Feel free to
# update this order as picks are traded.
def user_choice_draft_list():
    draft_list = ["1. Jacksonville Jaguars", "2. Detroit Lions",
                  "3. Houston Texans", "4. New York Jets",
                  "5. New York Giants", "6. Carolina Panthers",
                  "7. New York Giants (from CHI)", "8. Atlanta Falcons",
                  "9. Seattle Seahawks (from DEN)",
                  "10. New York Jets (from SEA)", "11. Washington Commanders",
                  "12. Minnesota Vikings", "13. Houston Texans (from CLE)",
                  "14. Baltimore Ravens",
                  "15. Philadelphia Eagles (from MIA)",
                  "16. Philadelphia Eagles (from IND)",
                  "17. Los Angeles Chargers",
                  "18. New Orleans Saints", "19. Philadelphia Eagles",
                  "20. Pittsburgh Steelers",
                  "21. New England Patriots",
                  "22. Green Bay Packers (from LV)", "23. Arizona Cardinals",
                  "24. Dallas Cowboys", "25. Buffalo Bills",
                  "26. Tennessee Titans", "27. Tampa Bay Buccaneers",
                  "28. Green Bay Packers",
                  "29. Kansas City Chiefs (from SF via MIA)",
                  "30. Kansas City Chiefs",
                  "31. Cincinnati Bengals", "32. Detroit Lions (from LAR)"]
    for draft in range(32):
        print(draft_list[draft])


# The main function allows the user to choose to evaluate offense or defense,
# print the draft order, or kill the program.
def main():
    kill_program = False
    print(
        "This program is a tool designed to help NFL teams make smart draft"
        " choices in the first round.")
    while not kill_program:
        user_input = input(
            "Please enter \"OFFENSE\" or \"DEFENSE\" to evaluate a player. "
            "Enter \"DRAFT ORDER\" to see the order of the draft. Enter "
            "\"STOP\" to end the program: ")
        if user_input.lower() == "stop":
            kill_program = True
        elif user_input.lower() == "offense":
            user_choice_offense()
        elif user_input.lower() == "defense":
            user_choice_defense()
        elif user_input.lower() == "kicker" or user_input.lower() == "punter" \
                or user_input.lower() == "special teams":
            print(
                "Kickers, punters, and long-snappers are not worth first round"
                " draft picks.")
        elif user_input.lower() == "draft order":
            user_choice_draft_list()
        else:
            print("That was not a valid entry.")


main()
