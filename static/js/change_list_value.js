// фунции для редактирования листов в форме "словосочетания"
        
// изменить текущее значение выбранного пункта в форме (срабатывает при двойном клике) 
function change_list1_values() {
	var selectBox = document.getElementById("list1");
	var selectedText = selectBox.options[selectBox.selectedIndex].text;
	var list1_text = prompt("Изменить значение ", selectedText);
	if (list1_text == null || list1_text == "") {
	
	} else {
		alert("Вы изменили словосочетание:\n'" + selectedText + "' на\n'"+ list1_text + "'");
		selectBox.options[selectBox.selectedIndex].text = list1_text;
	}
}
