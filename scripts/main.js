const articleTypeLoad = () => {
   const div = document.getElementById("contents");
   fetch("./scripts/articles.json")
   .then((response) => response.json())
   .then(articlesObject => {
      const articleTypes = Object.keys(articlesObject);
      console.log(articleTypes);
      articleTypes.forEach((articleType) => {
         const fileLocation = "./html/" + articleType + "/index.html";
         console.log(fileLocation);
         articleType = capitalise(articleType);

         const header = document.createElement("h3");
         const anchor = document.createElement("a");
         anchor.href = fileLocation;
         anchor.innerHTML = articleType;
         
         header.appendChild(anchor);
         div.appendChild(header);
      });
   });
}

const searchJson = () => {
   const searchInput = document.getElementById("searchInput").value.toLowerCase();
   const contents = document.getElementById("contents");
   const search = document.getElementById("search");
   const filters = {
      "settlements": document.getElementById("Locations").checked,
      "regions": document.getElementById("Locations").checked,
      "locations": document.getElementById("Locations").checked,
      "organisations": document.getElementById("Organisations").checked,
      "pcs": document.getElementById("PCs").checked,
      "npcs": document.getElementById("NPCs").checked,
      "lore": document.getElementById("Lore").checked
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
         articleTypes.forEach((articleType) => {
            // "settlements", "lore", ...
            if (!filters[articleType] && notAllFalse(filters)) {
               return;
            }
            const articles = infoObject[articleType];
            const articleTitles = Object.keys(articles);
            if (articleTitles.length > 0) {
               articleTitles.forEach((articleTitle) => {
                  // "trimor", "creswell", ...
                  const page = document.createElement("div");
                  const articleContents = articles[articleTitle];
                  const sections = Object.keys(articleContents);
                  sections.forEach((section) => {
                     // "Demographics", "Government", ...
                     const description = articleContents[section];
                     if (
                        section.toLowerCase().includes(searchInput) || 
                        description.toLowerCase().includes(searchInput)
                     ) {
                        if (page.innerHTML === "") {
                           // Move this out of for loop?
                           const title = document.createElement("h3");
                           const titleLink = document.createElement("a");
                           titleLink.href = "./html/" + articleType + "/" + articleTitle + ".html";
                           titleLink.onclick = clearSearch;
                           titleLink.innerHTML = capitalise(articleTitle);
                           title.appendChild(titleLink);
                           page.appendChild(title);
                        }
                        if (section === "Backstory") {
                           // Backstories are too large and clog up search results,
                           //   but include page in results
                           return;
                        }
                        const sectionHeader = document.createElement("h4");
                        sectionHeader.innerHTML = section;
                        page.appendChild(sectionHeader);
                        const sectionContents = document.createElement("p");
                        sectionContents.innerHTML = description;
                        page.appendChild(sectionContents);
                     }
                  });
                  if (page.innerHTML !== "") {
                     if (count > 0) {
                        const line = document.createElement("hr");
                        search.appendChild(line);
                     } count++;
                     search.appendChild(page);
                  }
               });
            }
         });
      });
   }
}

const clearSearch = () => {
   document.getElementById("searchInput").value = "";
}

const capitalise = aString => {
   aString = aString.charAt(0).toUpperCase() + aString.slice(1, aString.length);
   for (let i = 0; i < aString.length; i++) {
      if (aString.charAt(i) == "-") {
         aString = aString.slice(0, i) + " " + aString.charAt(i + 1).toUpperCase() + aString.slice(i + 2, aString.length);
      }
   } return aString;
};

const notAllFalse = (filters) => {
   const values = Object.values(filters);
   for (let value of values) {
      if (value) {
         return true;
      }
   } return false;
}

const openNotes = () => {
   // change this to "showNotes()" and have this available on all pages
   document.getElementById("searchInput").value = "";
   searchJson();
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
   articleTypeLoad();
}