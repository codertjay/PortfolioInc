function getToken (name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split (';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim ();
            // Does this cookie string begin with the name we want?
            if (cookie.substring (0 , name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent (cookie.substring (name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getToken ('csrftoken')

/*

contact_name
contact_email
contact_subject
contact_message

*/
const host = "{{ domain }}"

const formElem = document.querySelector ('form')
formElem.addEventListener ('submit' , event => {
    event.preventDefault ()
    let post_url = `http://www.localhost:8000/user/contactuser/`
    const method = 'POST'
    const formData = new FormData ()
    console.log (document.getElementById ('contact_name').value)
    formData.append ('contact_name' , document.getElementById ('contact_name').value)
    formData.append ('contact_email' , document.getElementById ('contact_email').value)
    formData.append ('contact_subject' , document.getElementById ('contact_subject').value)
    formData.append ('contact_message' , document.getElementById ('contact_message').value)
    formData.append ('to_email' , document.getElementById ('to_email').value)

    console.log (formData)
    $.ajax ({
        url: post_url ,
        type: method ,
        headers: {'X-CSRFTOKEN': csrftoken} ,
        data: formData ,
        contentType: false ,
        cache: false ,
        processData: false ,
        success: function (response) {
            alert ('success' , response)
        } ,
        error: function (response) {
            alert (response.responseText)
            console.log (response)
        }
    }).done (function (response) {
        console.log ('response' , response.statusText)
        document.getElementById ('contact_name').value = ''
        document.getElementById ('contact_email').value = ''
        document.getElementById ('contact_subject').value = ''
        document.getElementById ('contact_message').value = ''
    })

})