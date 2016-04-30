		<script>
			function getTweets() {
				$.ajax({
					url: "http://192.168.1.7:5000/ajax/wall/{{name}}",
					dataType: "json",
					async: false,
					success: function (data) {
						console.log(data);
						for (i=0; i<data.statuses.length; i++) {
							var unshiftValue = "<section class=\"grid-wrap\">";
							unshiftValue += "<ul class=\"grid\">";
							unshiftValue += "<li class=\"grid-sizer\">";
							unshiftValue += "</li>";
							unshiftValue += "<figure>";
							unshiftValue += "<img src=\" "+data.statuses[i].user.profile_image_url_https+ "\" alt=\"\" >";
							unshiftValue += "<figcaption>";
							unshiftValue += "<p>";
							unshiftValue += "<h3>";
							unshiftValue += data.statuses[i].user.screen_name;
							unshiftValue += "</h3>";
							unshiftValue += data.statuses[i].text;
							unshiftValue += "</p>";
							unshiftValue += "</figcaption>";
							unshiftValue += "</li>";
							unshiftValue += "</ul>";
							unshiftValue += "</section>";
							$('.wall').append(unshiftValue);
						}
					}
				});
				new CBPGridGallery( document.getElementById( 'grid-gallery' ) );
			}
			setInterval( getTweets, 30000 );
		</script>