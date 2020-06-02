def view_all():
    all_tasks = open("tasks.txt","r")
    num = 1
    for line in all_tasks:
        temp = line.strip()
        temp = temp.split(", ")
        print("")
        print("{}   TASK USER              :{}".format(num,temp[0]))
        print("    TASK NAME              :{}".format(temp[1]))
        print("    DESCRIPTION            :{}".format(temp[2]))
        print("    DATE ASSIGNED          :{}".format(temp[3]))
        print("    DATE DUE               :{}".format(temp[4]))
        print("    COMPLETION STATUS      :{}".format(temp[5]))
        num += 1
    all_tasks.close()
