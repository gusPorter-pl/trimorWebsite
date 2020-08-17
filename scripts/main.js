const search = () => {
   const searchInput = document.getElementById("searchInput").value.toLowerCase();
   const contents = document.getElementById("contents");
   const search = document.getElementById("search");
   const filters = {
      "settlements": document.getElementById("Locations").checked,
      "lore": document.getElementById("Lore").checked,
      "npcs": document.getElementById("NPCs").checked,
      "pcs": document.getElementById("PCs").checked,
      "organisations": document.getElementById("Organisations").checked
   };
   
   search.innerHTML = "";
   if (searchInput === "") {
      contents.style.display = "block";
      search.style.display = "none";
   } else {
      search.style.display = "block";
      contents.style.display = "none";
      fetch("./scripts/info.json")
      .then((response) => response.json())
      .then(infoObject => {
         const articleTypes = Object.keys(infoObject);
         let count = 0;
         for (let articleType of articleTypes) {
            // "settlements", "lore", ...
            if (!filters[articleType] && notAllFalse(filters)) {
               continue;
            }
            let articles = infoObject[articleType];
            let articleTitles = Object.keys(articles);
            if (articleTitles.length > 0) {
               for (let articleTitle of articleTitles) {
                  // "trimor", "creswell", ...
                  let page = document.createElement("div");
                  let articleContents = articles[articleTitle];
                  let sections = Object.keys(articleContents);
                  for (let section of sections) {
                     // "Demographics", "Government", ...
                     let description = articleContents[section];
                     if (
                        section.toLowerCase().includes(searchInput) || 
                        description.toLowerCase().includes(searchInput)
                     ) {
                        if (page.innerHTML === "") {
                           let title = document.createElement("h3");
                           let titleLink = document.createElement("a");
                           titleLink.href = "./html/" + articleType + "/" + articleTitle + ".html";
                           titleLink.onclick = clearSearch;
                           titleLink.innerHTML = capitalise(articleTitle);
                           title.appendChild(titleLink);
                           page.appendChild(title);
                        }
                        let sectionHeader = document.createElement("h4");
                        sectionHeader.innerHTML = section;
                        page.appendChild(sectionHeader);
                        let sectionContents = document.createElement("p");
                        sectionContents.innerHTML = description;
                        page.appendChild(sectionContents);
                     }
                  }
                  if (page.innerHTML !== "") {
                     if (count > 0) {
                        let line = document.createElement("hr");
                        search.appendChild(line);
                     } count++;
                     search.appendChild(page);
                  }
               }
            }
         }
      });
   }
}

const clearSearch = () => {
   document.getElementById("searchInput").value = "";
}

const capitalise = aString => aString.charAt(0).toUpperCase() + aString.slice(1, aString.length);

const notAllFalse = (filters) => {
   const values = Object.values(filters);
   for (let value of values) {
      if (value) {
         return true;
      }
   } return false;
}

const showFilters = () => {
   const showFilterButton = document.getElementById("showFilters");
   const hideFilterButton = document.getElementById("hideFilters");
   showFilterButton.style.display = "none";
   hideFilterButton.style.display = "block";
}

const hideFilters = () => {
   const showFilterButton = document.getElementById("showFilters");
   const hideFilterButton = document.getElementById("hideFilters");
   showFilterButton.style.display = "block";
   hideFilterButton.style.display = "none";
}

window.onload = () => {
   // document.getElementById("contents").style.display = "block";
   // document.getElementById("search").style.display = "none";
   // document.getElementById("showFilters").style.display = "block";
   // document.getElementById("hideFilters").style.display = "none";
}