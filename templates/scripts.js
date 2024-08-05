  $(document).ready(function() {
      $(".accordion").click(function() {
          $(this).next(".panel:first").slideToggle("fast");
      });

      $(".select-all-btn").click(function() {
          let panel = $(this).closest(".content, .questions");
          let checkboxes = panel.find("input[type='checkbox']");
          let allChecked = checkboxes.filter(":checked").length === checkboxes.length;

          checkboxes.prop("checked", !allChecked);
      });

      $("#multiSelectForm").submit(function(event) {
          event.preventDefault(); // Prevent the default form submission

          let selectedOptions = [];
          $("input[type='checkbox']:checked").each(function() {
              selectedOptions.push($(this).val());
          });
          console.log("Selected options: " + selectedOptions.join(", "));

          // Optionally, you can send the data to a server or handle it here
      });
  });
