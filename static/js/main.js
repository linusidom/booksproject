// console.dir(document.location.pathname)

// Remove Div on Index Page
if (document.location.pathname === '/'){
	let div = document.querySelector('#content')
	div.style.display = 'none';
}