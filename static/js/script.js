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


// == Delete-button handler ==
// Helper to get CSRF token from cookies
function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

document.addEventListener('DOMContentLoaded', () => {
	const deleteButtons = document.querySelectorAll('.btn-delete');

	deleteButtons.forEach((btn) => {
		btn.addEventListener('click', (e) => {
			const id = btn.dataset && btn.dataset.id ? btn.dataset.id : btn.getAttribute('data-id');
			if (!id) {
				console.warn('Delete button clicked but no data-id found on element:', btn);
				return;
			}

			// Confirm before deleting
			if (window.confirm('Are you sure you want to delete this article?')) {
				const csrftoken = getCookie('csrftoken');
				
				// Send DELETE request
				fetch(`/articles/${id}/delete/`, {
					method: 'POST',
					headers: {
						'X-CSRFToken': csrftoken,
					},
				})
				.then(response => {
					if (response.ok || response.status === 302) {
						// Show success toast
						showDeleteToast();
						
						// Redirect after a brief delay to show the toast
						setTimeout(() => {
							window.location.href = '/my_submissions/';
						}, 1500);
					} else {
						alert('Error deleting article');
					}
				})
				.catch(error => {
					console.error('Error:', error);
					alert('Error deleting article');
				});
			}
		});
	});
});


// == Toast notification function ==
function showDeleteToast() {
	const toastEl = document.getElementById('deleteToast');
	if (toastEl) {
		const toast = new bootstrap.Toast(toastEl);
		toast.show();
	}
}



