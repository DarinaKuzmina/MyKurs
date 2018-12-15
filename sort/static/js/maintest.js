var boxElements = document.getElementsByClassName('box'),
	boxElementsLength = boxElements.length,
	i;

for (i = 0; i < boxElementsLength; i++) {
	boxElements[i].classList.add('move');
}