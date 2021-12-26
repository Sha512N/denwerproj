function changeSearchType() { 
    searchType = document.getElementById("additionalSearchFieids");
    buttonText = document.getElementById("searchTypeButton");
    if (searchType.style.display != "inline") {
        searchType.style.display = "inline";
        buttonText.innerText = "Простой поиск";
        
    } else {
        searchType.style.display = "none";
        buttonText.innerText = "Расширенный поиск";
        
        document.getElementById("anacrusisCheckBox").checked = false;
        document.getElementById("clausulaCheckBox").checked = false;
        document.getElementById("additionalmrstatisticCheckBox").checked = false;
    }
}