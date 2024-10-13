
function addClassById(elementId, className) {
    
    // Get the element by its ID
    var element = document.getElementById(elementId);
    
    // Check if the element exists
    if (element) {
        // Add the class to the element
       
        element.classList.add(className);
    } else {
        console.log("Element not found with ID:", elementId);
    }
}
const today = new Date();

// Format the date to '11th Oct' format
const options = { day: 'numeric', month: 'long'  };
const formattedDate = today.toLocaleDateString('en-US', options);

// Add the date suffix (st, nd, rd, th)
function getDayWithSuffix(date) {
    const day = date.getDate();
    if (day > 3 && day < 21) return day + 'th'; // Exceptions for 11th to 13th
    switch (day % 10) {
        case 1: return day + 'st';
        case 2: return day + 'nd';
        case 3: return day + 'rd';
        default: return day + 'th';
    }
}

// Apply the suffix to the day
const dayWithSuffix = getDayWithSuffix(today);

console.log("running")
document.getElementById('dateHeading').textContent = dayWithSuffix + ', ' + formattedDate.split(' ')[0];