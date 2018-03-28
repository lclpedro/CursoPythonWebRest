function initConfig($scope, $http){
    console.log('Carregamento OK!')
    let api = 'http://localhost:5000/api'
    let get_contacts = ()=>{
        $http.get(`${api}/contacts`).then(data=>{
            $scope.list_contacts=data.data;
        })
    }
    get_contacts();

    $scope.insert_contact = (contact)=>{
        $http.post(`${api}/contacts`, contact).then(data=>{
            console.log(data)
            swal({
              title: "Muito bem!",
              text: data.data,
              icon: "success",
              button: "Fechar",
          });
            get_contacts();
            $scope.contact=null
        })
    }

    $scope.delete_contact=(data)=>{
        swal({
            title: "Você quer mesmo excluir?",
            text: `Se você confirmar, o contato de ${data.name_person} será excluido da sua lista de contatos.`,
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willDelete) => {
            if (willDelete) {
                swal(`Ok, Contato de ${data.name_person} deletado com Sucesso!`, {
                    icon: "success",
                });
            }
        });
    }

}
angular
.module('pythonWeb', [])
.controller('initConfigController', initConfig)