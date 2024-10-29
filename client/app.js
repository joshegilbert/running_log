console.log("connected");

// Elements and Variables
let runReviewWrapper = document.getElementById("run-review-wrapper");
let editId = null;
let inputRunTitle = document.getElementById("input-run-title");
let inputRunDistance = document.getElementById("input-run-distance");
let inputRunIntensity = document.getElementById("input-run-intensity");
let inputRunDescription = document.getElementById("input-run-description");
let inputRunWith = document.getElementById("input-run-with");
let inputRunGround = document.getElementById("input-run-ground");
let saveReviewButton = document.getElementById("save-review-button");
let addReviewButton = document.getElementById("add-review-button");
let totalMileageElement = document.getElementById("total-mileage-text");
let longestRunElement = document.getElementById("longest-run-text");

let totalMileage = 0;
let longestRun = 0;

// Function to play sound when adding a new run
function playSound() {
  let audio = new Audio("why_you_run.mp3");
  audio.play();
}

// Function to add a run review to the page and update total mileage and longest run
function addRunReview(data) {
  let runContainer = document.createElement("div");
  runContainer.classList.add("run-container");

  // Create run elements
  let runTitle = document.createElement("h3");
  runTitle.textContent = data["title"];
  let runDistance = document.createElement("p");
  runDistance.textContent = `Distance: ${data["distance"]} miles`;
  let runIntensity = document.createElement("p");
  runIntensity.textContent = `Intensity: ${data["intensity"]}`;
  let runDescription = document.createElement("p");
  runDescription.textContent = `Description: ${data["description"]}`;
  let runWith = document.createElement("p");
  runWith.textContent = `Run With: ${data["with"]}`;
  let runGround = document.createElement("p");
  runGround.textContent = `Ground: ${data["ground"]}`;

  runContainer.append(
    runTitle,
    runDistance,
    runIntensity,
    runDescription,
    runWith,
    runGround
  );

  // Calculate mileage
  let distanceValue = parseFloat(data["distance"]);
  totalMileage += distanceValue;
  if (distanceValue > longestRun) {
    longestRun = distanceValue;
  }
  updateTotals();

  // Edit and Delete buttons
  let editButton = document.createElement("button");
  editButton.textContent = "Edit Review";
  editButton.classList.add("edit");

  let deleteButton = document.createElement("button");
  deleteButton.textContent = "Delete Review";
  deleteButton.classList.add("delete");

  // Edit functionality
  editButton.onclick = () => {
    inputRunTitle.value = data["title"];
    inputRunDistance.value = data["distance"];
    inputRunIntensity.value = data["intensity"];
    inputRunDescription.value = data["description"];
    inputRunWith.value = data["with"];
    inputRunGround.value = data["ground"];
    editId = data["id"];
  };

  // Save edited review
  saveReviewButton.onclick = () => {
    let editData =
      "title=" +
      encodeURIComponent(inputRunTitle.value) +
      "&distance=" +
      encodeURIComponent(inputRunDistance.value) +
      "&intensity=" +
      encodeURIComponent(inputRunIntensity.value) +
      "&description=" +
      encodeURIComponent(inputRunDescription.value) +
      "&with=" +
      encodeURIComponent(inputRunWith.value) +
      "&ground=" +
      encodeURIComponent(inputRunGround.value);

    fetch(`http://localhost:8080/runs/${editId}`, {
      method: "PUT",
      body: editData,
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    }).then(() => {
      clearLoadedRuns();
      loadRunsFromServer();
      clearInputFields();
    });
  };

  // Delete functionality with confirmation
  deleteButton.onclick = () => {
    if (
      confirm(`Are you sure you want to delete the run "${data["title"]}"?`)
    ) {
      fetch(`http://localhost:8080/runs/${data["id"]}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      }).then(() => {
        clearLoadedRuns();
        loadRunsFromServer();
      });
    }
  };

  runContainer.append(editButton, deleteButton);
  runReviewWrapper.appendChild(runContainer);
}

// Function to update total mileage and longest run
function updateTotals() {
  totalMileageElement.textContent = `Total Mileage: ${totalMileage}`;
  longestRunElement.textContent = `Longest Run: ${longestRun}`;
}

// Load all runs from server
function loadRunsFromServer() {
  fetch("http://localhost:8080/runs")
    .then((response) => response.json())
    .then((data) => {
      data.forEach(addRunReview);
    });
}

// Clear loaded runs
function clearLoadedRuns() {
  runReviewWrapper.textContent = "";
}

// Clear input fields after saving or adding
function clearInputFields() {
  inputRunTitle.value = "";
  inputRunDistance.value = "";
  inputRunIntensity.value = "";
  inputRunDescription.value = "";
  inputRunWith.value = "";
  inputRunGround.value = "";
}

// Add new run review
function addNewReview() {
  let data =
    "title=" +
    encodeURIComponent(inputRunTitle.value) +
    "&distance=" +
    encodeURIComponent(inputRunDistance.value) +
    "&intensity=" +
    encodeURIComponent(inputRunIntensity.value) +
    "&description=" +
    encodeURIComponent(inputRunDescription.value) +
    "&with=" +
    encodeURIComponent(inputRunWith.value) +
    "&ground=" +
    encodeURIComponent(inputRunGround.value);

  fetch("http://localhost:8080/runs", {
    method: "POST",
    body: data,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  }).then(() => {
    clearLoadedRuns();
    loadRunsFromServer();
    clearInputFields();
  });
}

addReviewButton.onclick = () => {
  addNewReview();
  // playSound();
};
loadRunsFromServer();
