// from prev project:
// const editButtons = document.getElementsByClassName("btn-edit");
// const commentText = document.getElementById("id_body");
// const commentForm = document.getElementById("commentForm");
// const submitButton = document.getElementById("submitButton");

// from prev project:
// const deleteModal = new
// bootstrap.Modal(document.getElementById("deleteModal"));
// const deleteButtons = document.getElementsByClassName("btn-delete");
// const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/

// for (let button of editButtons) {
//     button.addEventListener("click", (e) => {
//         let commentId = e.target.getAttribute("comment_id");
//         let commentContent = document.getElementById(`comment${commentId}`).innerText;
//         commentText.value = commentContent;
//         submitButton.innerText = "Update";
//         commentForm.setAttribute("action", `edit_comment/${commentId}`);
//     });
// }

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
 */
// for (let button of deleteButtons) {
//     button.addEventListener("click", (e) => {
//         let commentId = e.target.getAttribute("comment_id");
//         deleteConfirm.href = `delete_comment/${commentId}`;
//         deleteModal.show()
//     })
// }




// == Edit-button navigation handler ==
// Buttons in the template use: class="btn btn-edit" data-id="{{ article.id }}"
document.addEventListener('DOMContentLoaded', () => {
	const editButtons = document.querySelectorAll('.btn-edit');

	editButtons.forEach((btn) => {
		btn.addEventListener('click', (e) => {
			// Prefer dataset (data-id) then fallback to attribute
			const id = btn.dataset && btn.dataset.id ? btn.dataset.id : btn.getAttribute('data-id');
			if (!id) {
				console.warn('Edit button clicked but no data-id found on element:', btn);
				return;
			}

			// Navigate to the edit page for the article
			window.location.href = `/articles/${id}/edit/`;
		});
	});
});



