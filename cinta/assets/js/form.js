function handleOnSubmit(e) {
    e.preventDefault();    
    let name = e.target.elements[0].value;
    let age = e.target.elements[1].value;
    let skills = e.target.elements[2].value.split(",");
    let pic1 = e.target.elements[3].value;
    let pic2 = e.target.elements[4].value;

    const formData = new FormData();

    formData.append('username', name);
    formData.append('age', age);
    formData.append('skills', skills);
    formData.append('pic1', pic1);
    formData.append('pic2', pic2);

    /* var csrftoken = getCookie('csrftoken');
    var headers = new Headers();
    headers.append('X-CSRFToken', csrftoken); */

    fetch('http://127.0.0.1:8000/upload', {
    method: 'POST',
    body: formData
    })
    .then(response => response.json())
    .then(result => {
    console.log('Success:', result);
    })
    .catch(error => {
    console.error('Error:', error); 
 });
};
