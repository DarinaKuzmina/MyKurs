function changeIcon() {
	document.getElementById("choosen_icon").src = document.getElementById("select_icon").value.split("_")[0];
};

window.onload = function() {
	changeIcon();
};