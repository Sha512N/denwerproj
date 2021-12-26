function activateNameFieid() {
    
    if (document.getElementById("poemNameCheckBox").checked) {
        document.getElementById("poemNamesList").disabled = false;          
    } 
    else {
        document.getElementById("poemNamesList").disabled = true;
    }
} 
function activateContextFieid() {
    
    if (document.getElementById("ContextCheckBox").checked) {
        document.getElementById("contextSearchInput").disabled = false;          
    } 
    else {
        document.getElementById("contextSearchInput").disabled = true;  
    }       
}
function activateAuthorsFieid() {
    
    if (document.getElementById("authorCheckBox").checked) {
        document.getElementById("authorsList").disabled = false;          
    } 
    else {
        document.getElementById("authorsList").disabled = true;  
    }       
}
function activateMrstatisticFieid() {
    
    if (document.getElementById("mrstatisticCheckBox").checked) {
        document.getElementById("mrstatisticType").disabled = false;
        document.getElementById("mrstatisticSymbol").disabled = false;
        document.getElementById("mrstatisticVolume").disabled = false;
    } 
    else {
        document.getElementById("mrstatisticType").disabled = true;
        document.getElementById("mrstatisticSymbol").disabled = true;
        document.getElementById("mrstatisticVolume").disabled = true;
    }       
}
function activateGenreFieid() {
    
    if (document.getElementById("genreCheckBox").checked) {
        document.getElementById("genreList").disabled = false;
    } 
    else {
        document.getElementById("genreList").disabled = true; 
    }       
}