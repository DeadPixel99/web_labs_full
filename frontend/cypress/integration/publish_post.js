describe("Test Post publishing", () => {
    beforeEach(() => {
        cy.visit('http://localhost:8000/login')
        cy.get("#id_username").type("test_user").should("have.value", "test_user")
        cy.get("#id_password").type("Pass1234!").should('have.value', "Pass1234!")
        cy.get('input[type="submit"]').click()
    })

    it("Test create post", () => {
        cy.get("textarea").type("test post").should("have.value", "test post")
        cy.get('button[type="submit"]').contains('Publish').click()
    })

    it("Post appeared", () => {
        cy.reload()
        cy.get("#post-text").contains('test post')
    })

})