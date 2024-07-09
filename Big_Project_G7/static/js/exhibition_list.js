document.addEventListener("DOMContentLoaded", function () {
  var calendarEl = document.getElementById("calendar");
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: "dayGridMonth",
    locale: "ko", // 한국어로 설정
    selectable: true,
    select: function (info) {
      var selectedDate = info.startStr;
      document.getElementById("selected-date").textContent =
        "선택한 날짜: " + selectedDate;
      fetchExhibitions(selectedDate);
      toggleCalendar();
    },
  });
  calendar.render();
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
        location.href = `{{ window.location.origin }}/${exhibition.ExhibitionURL}`;
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
  if (
    calendarContainer.style.display === "none" ||
    calendarContainer.style.display === ""
  ) {
    calendarContainer.style.display = "block";
    // FullCalendar 초기화
    var calendar = new FullCalendar.Calendar(
      document.getElementById("calendar"),
      {
        initialView: "dayGridMonth",
        locale: "ko",
        selectable: true,
        select: function (info) {
          var selectedDate = info.startStr;
          document.getElementById("selected-date").textContent =
            "선택한 날짜: " + selectedDate;
          fetchExhibitions(selectedDate);
          toggleCalendar();
        },
      }
    );
    calendar.render();
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
