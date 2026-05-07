from pyscript import document, display # type: ignore
import matplotlib.pyplot as plt
import logging

logging.getLogger('matplotlib').setLevel(logging.ERROR)

# set the days and absenses for the graph
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
absences = [0, 0, 0, 0, 0]

fig, ax = plt.subplots(figsize=(6,4))
line, = ax.plot(week_days, absences, marker='o')

# Set labels of the graph
ax.set_title('Absences by Day')
ax.set_xlabel('Day')
ax.set_ylabel('Absences')
ax.grid(True)

# Display the graph
display(fig, target="graphHolder")


def sample_numpy(e):
    # gets the inputs values
    day = document.getElementById("day").value
    absence_input = document.getElementById("absences").value

    # check if the day is selected and the input is not empty
    if day != "select days" and absence_input:
        try:
            absence_count = int(absence_input)
            index = week_days.index(day)
            absences[index] = absence_count

            line.set_ydata(absences)
            ax.relim()
            ax.autoscale_view()

            display(fig, target="graphHolder", append=False)

            # Clear input field
            document.getElementById("absences").value = ""

        except:
            print("Invalid input")
    else:
        print("Select a day and enter absences")