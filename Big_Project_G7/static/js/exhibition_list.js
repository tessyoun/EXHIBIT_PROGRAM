document.addEventListener("DOMContentLoaded", function () {
  let monthToday = (new Date().getMonth() + 1).toString();
if (monthToday.length === 1) {
  monthToday = "0" + monthToday.toString();
}
const newEventsData = eventsData.map((event) => {
  event.start = event.start.split("");
  event.start.splice(5, 2, monthToday);
  event.start = event.start.join("");
  event.end = event.end.split("");
  event.end.splice(5, 2, monthToday);
  event.end = event.end.join("");
  return event;
});

// Creates calendar
new Calendar({
  id: "#color-calendar",
  primaryColor: "#04AFDF",
  theme: "glass",
  border: "7px solid #04AFDF",
  weekdayType: "long-upper",
  monthDisplayType: "long",
  headerBackgroundColor: "#04AFDF",
  eventsData: newEventsData,
  dateChanged: (currentDate, events) => {
    const eventDisplay = document.getElementById("events-display");
    let html = "";
    events.forEach((event) => {
      let from = new Date(event.start).toLocaleString([], {
        dateStyle: "medium",
        timeStyle: "short"
      });
      let to = new Date(event.end).toLocaleString([], {
        dateStyle: "medium",
        timeStyle: "short"
      });
      html += `
        <div class="event">
          <div class="event__name">${event.name}</div>
          <div class="event__datestart">From: ${from}</div>
          <div class="event__dateend">To: ${to}</div>
        </div>
      `;
    });
    eventDisplay.innerHTML = html;
  }
});














  var calendarEl = document.getElementById("calendar");
  console.log("calendarEl:", calendarEl);
  
  let test_calendar=new Calendar({
    id: '#color-calendar',
})
console.log(test_calendar);

  if (calendarEl) {
    var calendar = new Calendar(calendarEl, {
      id: '#color-calendar',
      theme: "glass",
      primaryColor: "#1a73e8",
      headerBackgroundColor: "#ffffff",
      weekdayType: "long",
      locale: "ko",
      selectable: true,
      select: function (info) {
        var selectedDate = info.startStr;
        document.getElementById("selected-date").textContent =
          "선택한 날짜: " + selectedDate;
        fetchExhibitions(selectedDate);
        toggleCalendar(); // Consider removing this call if not necessary
      }
    });

    calendar.render();
  } else {
    console.error("Calendar element not found in the DOM.");
  }
});


// 달력 외의 영역 클릭 시 달력 숨기기
window.addEventListener("click", function (e) {
  var calendarContainer = document.getElementById("calendar-container");
  var toggleButton = document.querySelector(".toggle-calendar-button");

  if (!calendarContainer.contains(e.target) && e.target !== toggleButton) {
    calendarContainer.style.display = "none";
  }
});

// Function to render exhibitions
function renderExhibitionList(exhibitionsData) {
  var exhibitions = JSON.parse(exhibitionsData);
  const exhibitionList = document.getElementById("exhibition-list");
  exhibitionList.innerHTML = ""; // Clear previous content
  if (exhibitions.length === 0) {
    exhibitionList.innerHTML = "<p>전시회가 없습니다.</p>";
  } else {
    exhibitions.forEach((exhibition) => {
      const exhibitionCard = document.createElement("div");
      exhibitionCard.className = "exhibition-card";
      exhibitionCard.onclick = function () {
        location.href = `${window.location.origin}/${exhibition.ExhibitionURL}`;
      };
      exhibitionCard.innerHTML = `
                          <div class="background-image" style="background-image: url('/static/${exhibition.ExhibitionImageURL}');"></div>
                          <div class="exhibition-details">
                              <h3>${exhibition.ExhibitionName}</h3>
                              <p>전시장: ${exhibition.Hall_ID__ExhibitionHallDescription}</p>
                              <p>기간: ${exhibition.ExhibitionRegistrationDate} ~ ${exhibition.ExhibitionClosedDate}</p>
                          </div>
                      `;
      exhibitionList.appendChild(exhibitionCard);
    });
  }
}

function toggleCalendar() {
  var calendarContainer = document.getElementById("calendar-container");
  
  if (!calendarContainer) return; // Ensure calendar container exists

  if (calendarContainer.style.display === "none" || calendarContainer.style.display === "") {
    calendarContainer.style.display = "block";
  } else {
    calendarContainer.style.display = "none";
  }
}

function fetchExhibitions(selectedDate = "") {
  var url = selectedDate
    ? "/exhibition/list/" + selectedDate + "/"
    : "/exhibition/list/";
  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      renderExhibitionList(data);
    })
    .catch((error) => console.error("Error:", error));
}
