const search = () => {
   const searchInput = document.getElementById("searchInput").value;
   const contents = document.getElementById("contents");
   const search = document.getElementById("search");
   if (searchInput === "") {
      contents.style.display = "block";
      search.style.display = "none";
      // Show articles based off of searchInput
   } else {
      search.style.display = "block";
      contents.style.display = "none";
      // clear search
   }
}

const showFilters = () => {
   const text = readFileSync("../html/maps/mapOfTrimor.html");
   console.log(text);
}

const hideFilters = () => {
}

window.onload = () => {
   // document.getElementById("contents").style.display = "block";
   // document.getElementById("search").style.display = "none";
   // document.getElementById("showFilters").style.display = "block";
   // document.getElementById("hideFilters").style.display = "none";
}