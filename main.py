from datetime import date, datetime

tasks = []

# Weekly available hours
weekly_hours = []


while True:

    print("\n====================================")
    print(" STUDENT WORKLOAD & DEADLINE ANALYZER")
    print("====================================")

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Analyze Workload & Make Weekly Plan")
    print("4. Progress & Task Management")
    print("5. Exit")

    choice = input("\nEnter your choice: ")


    # MODULE 1 - ADD TASK
    if choice == "1":

        print("\n--- ADD TASK ---")

        task_name = input("Enter task name: ")
        subject = input("Enter subject: ")


        while True:

            due_date_input = input(
                "Enter due date (DD-MM-YYYY): "
            )

            try:

                due_date = datetime.strptime(
                    due_date_input,
                    "%d-%m-%Y"
                ).date()

                if due_date < date.today():

                    print("Due date cannot be in the past.")

                else:
                    break

            except ValueError:

                print("Invalid date. Use DD-MM-YYYY.")


        while True:

            try:

                hours = float(
                    input("Enter estimated hours needed: ")
                )

                if hours <= 0:

                    print("Hours must be greater than 0.")

                else:
                    break

            except ValueError:

                print("Please enter a number.")


        while True:

            priority = input(
                "Enter priority (High/Medium/Low): "
            ).capitalize()

            if priority in ["High", "Medium", "Low"]:
                break

            print("Please enter High, Medium or Low.")


        tasks.append({
            "name": task_name,
            "subject": subject,
            "due_date": due_date,
            "hours": hours,
            "priority": priority,
            "status": "Not Started"
        })


        days_left = (
            due_date - date.today()
        ).days

        print("\nTask added successfully!")

        print(
            "Due date:",
            due_date.strftime("%d-%m-%Y")
        )

        print(
            "Days remaining:",
            days_left
        )


    # MODULE 2 - VIEW TASKS
    elif choice == "2":

        print("\n--- YOUR TASKS ---")

        if len(tasks) == 0:

            print("No tasks added yet.")

        else:

            print("\n" + "-" * 80)

            print(
                "No. | Task | Subject | Due Date | Days | Priority | Status"
            )

            print("-" * 80)


            for i in range(len(tasks)):

                task = tasks[i]

                days_left = (
                    task["due_date"] - date.today()
                ).days

                print(
                    i + 1,
                    "|",
                    task["name"],
                    "|",
                    task["subject"],
                    "|",
                    task["due_date"].strftime("%d-%m-%Y"),
                    "|",
                    days_left,
                    "|",
                    task["priority"],
                    "|",
                    task["status"]
                )

            print("-" * 80)


    # MODULE 3 - ANALYSIS AND WEEKLY PLAN
    elif choice == "3":

        print("\n--- WORKLOAD ANALYSIS ---")

        if len(tasks) == 0:

            print("No tasks available for analysis.")

        else:

            pending_tasks = []

            for task in tasks:

                if task["status"] != "Completed":

                    pending_tasks.append(task)


            if len(pending_tasks) == 0:

                print("\nAll your tasks are completed!")

            else:

                # DEADLINE DISTRIBUTION

                one_day = 0
                three_days = 0
                seven_days = 0
                later = 0


                for task in pending_tasks:

                    days_left = (
                        task["due_date"] - date.today()
                    ).days

                    if days_left <= 1:

                        one_day += 1

                    elif days_left <= 3:

                        three_days += 1

                    elif days_left <= 7:

                        seven_days += 1

                    else:

                        later += 1


                print("\nDeadline Distribution:")

                print(
                    "Due within 1 day :",
                    one_day
                )

                print(
                    "Due within 3 days:",
                    three_days
                )

                print(
                    "Due within 7 days:",
                    seven_days
                )

                print(
                    "Due later         :",
                    later
                )


                # WORKLOAD RISK

                high_priority = 0
                urgent = 0


                for task in pending_tasks:

                    days_left = (
                        task["due_date"] - date.today()
                    ).days

                    if task["priority"] == "High":

                        high_priority += 1

                    if days_left <= 3:

                        urgent += 1


                risk_score = (
                    high_priority + urgent * 2
                )


                if risk_score >= 6:

                    risk = "HIGH"

                elif risk_score >= 3:

                    risk = "MODERATE"

                else:

                    risk = "LOW"


                print(
                    "\nWorkload Risk:",
                    risk
                )


                # EARLY ATTENTION WARNING

                print(
                    "\nTasks needing early attention:"
                )

                found_warning = False


                for task in pending_tasks:

                    days_left = (
                        task["due_date"] - date.today()
                    ).days


                    if days_left > 0:

                        if task["hours"] / days_left >= 2:

                            print(
                                "→",
                                task["name"],
                                "- high effort for available time"
                            )

                            found_warning = True


                if found_warning == False:

                    print(
                        "No early-attention warnings."
                    )


                # TOP 3 FOCUS RECOMMENDATIONS

                print(
                    "\nTop 3 Focus Recommendations:"
                )


                sorted_tasks = pending_tasks.copy()


                for i in range(len(sorted_tasks)):

                    for j in range(
                        i + 1,
                        len(sorted_tasks)
                    ):

                        days1 = (
                            sorted_tasks[i]["due_date"]
                            - date.today()
                        ).days

                        days2 = (
                            sorted_tasks[j]["due_date"]
                            - date.today()
                        ).days


                        if days2 < days1:

                            temp = sorted_tasks[i]

                            sorted_tasks[i] = (
                                sorted_tasks[j]
                            )

                            sorted_tasks[j] = temp


                top_count = min(
                    3,
                    len(sorted_tasks)
                )


                for i in range(top_count):

                    task = sorted_tasks[i]

                    days_left = (
                        task["due_date"] - date.today()
                    ).days


                    print(
                        "\n",
                        i + 1,
                        ".",
                        task["name"]
                    )

                    print(
                        "   Due:",
                        task["due_date"].strftime(
                            "%d-%m-%Y"
                        )
                    )

                    print(
                        "   Days remaining:",
                        days_left
                    )

                    print(
                        "   Priority:",
                        task["priority"]
                    )


                    if task["priority"] == "High":

                        print(
                            "   Reason: High priority task."
                        )

                    elif days_left <= 3:

                        print(
                            "   Reason: Deadline is approaching."
                        )

                    else:

                        print(
                            "   Reason: Should be planned early."
                        )


                # WEEKEND DEADLINES

                print("\nWeekend Deadlines:")

                weekend_found = False


                for task in pending_tasks:

                    if task["due_date"].weekday() >= 5:

                        print(
                            "→",
                            task["name"],
                            "-",
                            task["due_date"].strftime(
                                "%d-%m-%Y"
                            ),
                            "(",
                            task["due_date"].strftime(
                                "%A"
                            ),
                            ")"
                        )

                        weekend_found = True


                if weekend_found == False:

                    print(
                        "No pending weekend deadlines."
                    )


                # WEEKLY AVAILABILITY
                # Ask only the first time.

                if len(weekly_hours) == 0:

                    print(
                        "\n--- WEEKLY AVAILABILITY ---"
                    )

                    print(
                        "Enter available study/work hours"
                    )

                    print(
                        "for each day of the next 7 days."
                    )


                    for i in range(7):

                        plan_date = date.fromordinal(
                            date.today().toordinal()
                            + i
                        )


                        while True:

                            try:

                                hours_available = float(
                                    input(
                                        plan_date.strftime(
                                            "%A %d-%m-%Y"
                                        )
                                        + " : "
                                    )
                                )


                                if hours_available < 0:

                                    print(
                                        "Hours cannot be negative."
                                    )

                                else:

                                    weekly_hours.append(
                                        hours_available
                                    )

                                    break

                            except ValueError:

                                print(
                                    "Please enter a number."
                                )


                else:

                    print(
                        "\nUsing your saved weekly availability."
                    )


                # CREATE COPY OF AVAILABLE HOURS
                # So original availability stays saved.

                available_hours = weekly_hours.copy()


                # SORT TASKS BY DEADLINE

                planning_tasks = pending_tasks.copy()


                for i in range(
                    len(planning_tasks)
                ):

                    for j in range(
                        i + 1,
                        len(planning_tasks)
                    ):

                        first = planning_tasks[i]
                        second = planning_tasks[j]


                        first_days = (
                            first["due_date"]
                            - date.today()
                        ).days

                        second_days = (
                            second["due_date"]
                            - date.today()
                        ).days


                        swap = False


                        if second_days < first_days:

                            swap = True

                        elif (
                            second_days == first_days
                            and
                            second["priority"] == "High"
                            and
                            first["priority"] != "High"
                        ):

                            swap = True


                        if swap:

                            temp = planning_tasks[i]

                            planning_tasks[i] = (
                                planning_tasks[j]
                            )

                            planning_tasks[j] = temp


                # CREATE EMPTY WEEK

                weekly_plan = []

                for i in range(7):

                    weekly_plan.append([])


                # PLAN TASKS

                for task in planning_tasks:

                    hours_left = task["hours"]


                    for day_index in range(7):

                        if hours_left <= 0:

                            break


                        plan_date = date.fromordinal(
                            date.today().toordinal()
                            + day_index
                        )


                        # Do not put work after deadline.

                        if plan_date > task["due_date"]:

                            break


                        free_hours = (
                            available_hours[day_index]
                        )


                        if free_hours > 0:

                            used_hours = min(
                                hours_left,
                                free_hours
                            )


                            weekly_plan[
                                day_index
                            ].append({
                                "name": task["name"],
                                "hours": used_hours
                            })


                            available_hours[
                                day_index
                            ] -= used_hours


                            hours_left -= used_hours


                    if hours_left > 0:

                        print(
                            "\nWARNING:",
                            task["name"],
                            "could not be fully scheduled."
                        )

                        print(
                            "Remaining hours:",
                            round(
                                hours_left,
                                2
                            )
                        )


                # SHOW GENERATED PLAN

                print(
                    "\n===================================="
                )

                print(
                    " AUTOMATIC 7-DAY WORK PLAN"
                )

                print(
                    "===================================="
                )


                daily_totals = []


                for day_index in range(7):

                    plan_date = date.fromordinal(
                        date.today().toordinal()
                        + day_index
                    )


                    print(
                        "\n",
                        plan_date.strftime(
                            "%A %d-%m-%Y"
                        )
                    )


                    day_total = 0


                    if len(
                        weekly_plan[day_index]
                    ) == 0:

                        print(
                            "  No tasks planned."
                        )

                    else:

                        for item in weekly_plan[
                            day_index
                        ]:

                            print(
                                "  •",
                                item["name"],
                                "-",
                                round(
                                    item["hours"],
                                    2
                                ),
                                "hrs"
                            )

                            day_total += (
                                item["hours"]
                            )


                    daily_totals.append(
                        day_total
                    )


                    print(
                        "  Total:",
                        round(
                            day_total,
                            2
                        ),
                        "hrs"
                    )


                # WEEKLY DISTRIBUTION

                print(
                    "\n--- WEEKLY WORKLOAD DISTRIBUTION ---"
                )


                for i in range(7):

                    plan_date = date.fromordinal(
                        date.today().toordinal()
                        + i
                    )

                    print(
                        plan_date.strftime("%A"),
                        ":",
                        round(
                            daily_totals[i],
                            2
                        ),
                        "hrs"
                    )


                # BUSIEST AND LIGHTEST DAY

                busiest_index = 0
                lightest_index = 0


                for i in range(7):

                    if (
                        daily_totals[i]
                        > daily_totals[busiest_index]
                    ):

                        busiest_index = i


                    if (
                        daily_totals[i]
                        < daily_totals[lightest_index]
                    ):

                        lightest_index = i


                busiest_date = date.fromordinal(
                    date.today().toordinal()
                    + busiest_index
                )

                lightest_date = date.fromordinal(
                    date.today().toordinal()
                    + lightest_index
                )


                print(
                    "\nBusiest day:",
                    busiest_date.strftime("%A"),
                    "-",
                    round(
                        daily_totals[busiest_index],
                        2
                    ),
                    "hrs"
                )


                print(
                    "Lightest day:",
                    lightest_date.strftime("%A"),
                    "-",
                    round(
                        daily_totals[lightest_index],
                        2
                    ),
                    "hrs"
                )


                # OVERLOAD / UNUSED TIME

                print(
                    "\n--- DAILY CAPACITY CHECK ---"
                )


                overload_found = False


                for i in range(7):

                    planned = daily_totals[i]
                    capacity = weekly_hours[i]


                    plan_date = date.fromordinal(
                        date.today().toordinal()
                        + i
                    )


                    if planned > capacity:

                        print(
                            "Warning:",
                            plan_date.strftime("%A"),
                            "is overloaded by",
                            round(
                                planned - capacity,
                                2
                            ),
                            "hrs."
                        )

                        overload_found = True

                    else:

                        free = capacity - planned

                        print(
                            plan_date.strftime("%A"),
                            ":",
                            round(
                                free,
                                2
                            ),
                            "hrs free"
                        )


                if overload_found == False:

                    print(
                        "\nNo workload overload detected."
                    )


                print(
                    "\nTotal work planned this week:",
                    round(
                        sum(daily_totals),
                        2
                    ),
                    "hrs"
                )


    # MODULE 4 - PROGRESS & TASK MANAGEMENT
    elif choice == "4":

        print(
            "\n--- PROGRESS & TASK MANAGEMENT ---"
        )


        if len(tasks) == 0:

            print("No tasks available.")

        else:

            print("\n1. Update Task Status")
            print("2. Edit Task")
            print("3. Delete Task")
            print("4. Progress Summary")
            print("5. Back")


            manage_choice = input(
                "\nEnter your choice: "
            )


            # UPDATE STATUS
            if manage_choice == "1":

                print("\n--- UPDATE STATUS ---")


                for i in range(len(tasks)):

                    print(
                        i + 1,
                        ".",
                        tasks[i]["name"],
                        "-",
                        tasks[i]["status"]
                    )


                try:

                    number = int(
                        input("\nEnter task number: ")
                    )


                    if (
                        number >= 1
                        and number <= len(tasks)
                    ):

                        print("\n1. Not Started")
                        print("2. In Progress")
                        print("3. Completed")


                        status_choice = input(
                            "Enter status: "
                        )


                        if status_choice == "1":

                            tasks[
                                number - 1
                            ]["status"] = "Not Started"


                        elif status_choice == "2":

                            tasks[
                                number - 1
                            ]["status"] = "In Progress"


                        elif status_choice == "3":

                            tasks[
                                number - 1
                            ]["status"] = "Completed"


                        else:

                            print(
                                "Invalid status."
                            )


                        print(
                            "\nStatus updated:",
                            tasks[
                                number - 1
                            ]["status"]
                        )


                    else:

                        print(
                            "Invalid task number."
                        )


                except ValueError:

                    print(
                        "Please enter a number."
                    )


            # EDIT TASK
            elif manage_choice == "2":

                print("\n--- EDIT TASK ---")


                for i in range(len(tasks)):

                    print(
                        i + 1,
                        ".",
                        tasks[i]["name"]
                    )


                try:

                    number = int(
                        input("\nEnter task number: ")
                    )


                    if (
                        number >= 1
                        and number <= len(tasks)
                    ):

                        task = tasks[
                            number - 1
                        ]


                        print(
                            "\nPress Enter to keep "
                            "the old value."
                        )


                        new_name = input(
                            "Task name ["
                            + task["name"]
                            + "]: "
                        )


                        new_subject = input(
                            "Subject ["
                            + task["subject"]
                            + "]: "
                        )


                        new_date = input(
                            "Due date ["
                            + task["due_date"].strftime(
                                "%d-%m-%Y"
                            )
                            + "]: "
                        )


                        new_hours = input(
                            "Estimated hours ["
                            + str(task["hours"])
                            + "]: "
                        )


                        new_priority = input(
                            "Priority ["
                            + task["priority"]
                            + "]: "
                        )


                        if new_name != "":

                            task["name"] = new_name


                        if new_subject != "":

                            task["subject"] = new_subject


                        if new_date != "":

                            try:

                                new_due_date = (
                                    datetime.strptime(
                                        new_date,
                                        "%d-%m-%Y"
                                    ).date()
                                )


                                if (
                                    new_due_date
                                    >= date.today()
                                ):

                                    task[
                                        "due_date"
                                    ] = new_due_date

                                else:

                                    print(
                                        "Date is in the past."
                                        " Old date kept."
                                    )


                            except ValueError:

                                print(
                                    "Invalid date."
                                    " Old date kept."
                                )


                        if new_hours != "":

                            try:

                                new_hours_value = (
                                    float(new_hours)
                                )


                                if (
                                    new_hours_value > 0
                                ):

                                    task[
                                        "hours"
                                    ] = new_hours_value

                                else:

                                    print(
                                        "Invalid hours."
                                        " Old value kept."
                                    )


                            except ValueError:

                                print(
                                    "Invalid hours."
                                    " Old value kept."
                                )


                        if new_priority != "":

                            new_priority = (
                                new_priority.capitalize()
                            )


                            if new_priority in [
                                "High",
                                "Medium",
                                "Low"
                            ]:

                                task[
                                    "priority"
                                ] = new_priority

                            else:

                                print(
                                    "Invalid priority."
                                    " Old value kept."
                                )


                        print(
                            "\nTask updated successfully!"
                        )


                    else:

                        print(
                            "Invalid task number."
                        )


                except ValueError:

                    print(
                        "Please enter a number."
                    )


            # DELETE TASK
            elif manage_choice == "3":

                print("\n--- DELETE TASK ---")


                for i in range(len(tasks)):

                    print(
                        i + 1,
                        ".",
                        tasks[i]["name"]
                    )


                try:

                    number = int(
                        input("\nEnter task number: ")
                    )


                    if (
                        number >= 1
                        and number <= len(tasks)
                    ):

                        deleted = tasks.pop(
                            number - 1
                        )


                        print(
                            "\nDeleted:",
                            deleted["name"]
                        )


                    else:

                        print(
                            "Invalid task number."
                        )


                except ValueError:

                    print(
                        "Please enter a number."
                    )


            # PROGRESS SUMMARY
            elif manage_choice == "4":

                completed = 0
                in_progress = 0
                not_started = 0


                for task in tasks:

                    if task["status"] == "Completed":

                        completed += 1

                    elif task["status"] == "In Progress":

                        in_progress += 1

                    else:

                        not_started += 1


                total = len(tasks)


                percentage = (
                    completed / total
                ) * 100


                print(
                    "\n--- PROGRESS SUMMARY ---"
                )


                print(
                    "Completed   :",
                    completed
                )

                print(
                    "In Progress :",
                    in_progress
                )

                print(
                    "Not Started :",
                    not_started
                )

                print(
                    "Overall completion:",
                    round(
                        percentage,
                        1
                    ),
                    "%"
                )


            elif manage_choice == "5":

                print(
                    "Going back to main menu."
                )


            else:

                print(
                    "Invalid choice."
                )


    # EXIT
    elif choice == "5":

        print(
            "\nThank you for using the "
            "Student Workload & Deadline Analyzer!"
        )

        break


    else:

        print(
            "\nInvalid choice. Please select 1-5."
        )

