# Run Tracker

A simple application to track your running sessions, including distance, intensity, description, companions, and terrain type.

## Resource

**Run**

### Attributes:

- **title** (string): The title or name of the run.
- **distance** (float): The distance of the run in miles.
- **intensity** (string): The intensity level of the run (e.g., easy, medium, hard).
- **description** (string): A short description of the run.
- **with** (string): Name of the person or group you ran with.
- **ground** (string): Type of ground surface (e.g., trail, road, track).

### Schema

```sql
CREATE TABLE runs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  distance REAL,
  intensity TEXT,
  description TEXT,
  run_with TEXT,
  ground TEXT
);
```

## REST Endpoints

| Name                      | Method | Path         | Description                                 |
| ------------------------- | ------ | ------------ | ------------------------------------------- |
| Retrieve all run entries  | GET    | `/runs`      | Get a collection of all run entries         |
| Retrieve specific run     | GET    | `/runs/<id>` | Get details of a specific run by its ID     |
| Create new run entry      | POST   | `/runs`      | Add a new run entry                         |
| Update existing run entry | PUT    | `/runs/<id>` | Update details of an existing run by its ID |
| Delete run entry          | DELETE | `/runs/<id>` | Remove a run entry by its ID                |

## Usage

1. **Add a New Run**: Use the modal form to input run details, then save.
2. **Edit an Existing Run**: Click "Edit" on an existing run entry, update details in the modal form, and save.
3. **Delete a Run**: Click "Delete" to remove a run entry.
4. **View Total Mileage**: The application tracks and displays total mileage and longest run distance.

## Running the Application

1. Clone the repository.
2. Install any required dependencies.
3. Start the server and open the application in your browser.

## Project Structure

- **index.html**: The main HTML file for the app interface.
- **app.js**: JavaScript logic for managing runs and interfacing with the API.
- **styles.css**: Styling for the application, including modal and run entry display.

---

Happy running! 🏃
