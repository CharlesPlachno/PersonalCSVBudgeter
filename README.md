# PersonalCSVBudgeter
Takes csv files with transaction details and allows you to track a month by month budget

## Development Plan

### csvloader
1. Have an input folder where statements can be placed in csv format.
2. Running csvloader will place any new entries from loaded files into a main csv history file.
3. It will move the file to a "loaded" folder where we will keep some number of previously loaded files
4. The main csv history file will contain an extra column for "tags" such as groceries, bills, etc

### budget_viewer
1. Set a monthly budget for individual tags, monthly saving, and set monthly income
2. View current spending for month with regards to individual tags
3. Compare current spending to previous months

