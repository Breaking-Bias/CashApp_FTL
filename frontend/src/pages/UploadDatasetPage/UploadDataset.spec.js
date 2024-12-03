// import 'cypress-file-upload';

// describe("Upload Dataset E2E Test", () => {
//     beforeEach(() => {
//       // Visit the page where the UploadDataset component is rendered
//       cy.visit("/upload-dataset");
//     });
  
//     it("displays the upload dataset page correctly", () => {
//       // Check if the title and main elements are displayed
//       cy.contains("Upload Dataset").should("be.visible");
//       cy.get("[data-testid='test-file-input']").should("exist");
//       cy.get("[data-testid='upload-dataset-button']").should("exist");
//     });
  
//     it("shows an error message when no file is selected and upload is clicked", () => {
//       cy.get("[data-testid='upload-dataset-button']").click();
//       cy.contains("Please select a file to upload.").should("be.visible");
//     });
  
//     it("successfully uploads a file and displays a success message", () => {
//       // Mock the backend server response for the file upload
//       cy.intercept("POST", "https://breakingbiasbigboss.zapto.org/upload-dataset", {
//         statusCode: 200,
//         body: { message: "File uploaded successfully!" },
//       }).as("uploadFile");
  
//       // Simulate file selection
//       const testFile = new File(["sample content"], "test-file.csv", {
//         type: "text/csv",
//       });
//       cy.get("[data-testid='test-file-input']").attachFile(testFile);
  
//       // Click the upload button
//       cy.get("[data-testid='upload-dataset-button']").click();
  
//       // Wait for the mocked API call and check success message
//       cy.wait("@uploadFile");
//       cy.contains("File uploaded successfully!").should("be.visible");
//     });
  
//     it("shows an error message on failed upload", () => {
//       // Mock the backend server response for a failed file upload
//       cy.intercept("POST", "https://breakingbiasbigboss.zapto.org/upload-dataset", {
//         statusCode: 500,
//         body: { message: "Failed to upload the file. Server returned error." },
//       }).as("uploadFileFail");
  
//       // Simulate file selection
//       const testFile = new File(["sample content"], "test-file.csv", {
//         type: "text/csv",
//       });
//       cy.get("[data-testid='test-file-input']").attachFile(testFile);
  
//       // Click the upload button
//       cy.get("[data-testid='upload-dataset-button']").click();
  
//       // Wait for the mocked API call and check error message
//       cy.wait("@uploadFileFail");
//       cy.contains("Failed to upload the file. Server returned error.").should(
//         "be.visible"
//       );
//     });
  
//     it("navigates to the Home page when the 'Back' button is clicked", () => {
//       cy.get("button").contains("Back").click();
//       cy.url().should("eq", `${Cypress.config().baseUrl}/`);
//     });
  
//     it("navigates to the Graph page when the 'View Results' button is clicked", () => {
//       cy.get("button").contains("View Results").click();
//       cy.url().should("include", "/graph");
//     });
//   });
  