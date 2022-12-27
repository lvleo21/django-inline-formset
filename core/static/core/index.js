const createAlternative = () => {
    let number = getAlternativeNumber();
    return `
        <div class="row m-1" name="alternative">
            <div class="col">
                <div class="form-floating">
                    <input type="text" name="alternative_set-${number}-description" maxlength="255" class="form-control"
                        id="id_alternative_set-${number}-description" placeholder="Alternativa #${number}">
                    <label for="id_alternative_set-${number}-description">Descrição</label>
                </div>
            </div>
            <div class="col d-flex justify-content-center align-items-center">
                <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" role="switch" name="alternative_set-${number}-is_correct"
                    id="id_alternative_set-${number}-is_correct">
                    <label class="form-check-label" for="id_alternative_set-${number}-is_correct">Correta</label>
                </div>
            </div>


            <input type="hidden" name="alternative_set-${number}-id" id="id_alternative_set-${number}-id">
            <input type="hidden" name="alternative_set-${number}-question" id="id_alternative_set-${number}-question">
        </div>
    `
}

const getAlternativeNumber = () => {
    return document.getElementsByName("alternative").length;
}

window.onload = () => {
    let alternativesBox = document.getElementById("alternative-box");
    console.log(alternativesBox)
    document.getElementById("add-alternative").addEventListener("click", (event) => {
        alternativesBox.insertAdjacentHTML("beforeend", createAlternative());

    })



}