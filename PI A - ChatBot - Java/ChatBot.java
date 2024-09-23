import java.util.Scanner;
public class ChatBot {
    public static void main(String[] args) {

        String menu1 = "Célia: Olá! Seja bem-vindo à nossa clínica médica. Sou Célia, sua atendente virtual. \n Como posso ajudar você hoje? \n 1 - Agendamentos e Consultas \n 2 - Informações sobre serviços \n 3 - Falar com um atendente \n 0-Encerrar atendimento";
        String menuAgenda = "Célia: Ótimo! O que você gostaria de fazer? \n 1 - Agendar uma consulta \n 2 - Cancelar uma consulta \n";
        String menuMarca = "Célia: Para agendar uma consulta, por favor, informe a especialidade que você precisa.\n 1 - Clínica Geral\n 2 - Pediatria\n 3 - Ginecologia\n 4 - Cardiologia\n 5 - Dermatologia\n";
        String menuInfo = "Célia: Que tipo de informação sobre nossos serviços você gostaria?\n 1 - Consultas médicas\n 2 - Exames laboratoriais\n 3 - Vacinas disponíveis\n";
        String menuInfoConsulta = "Célia: \n 1 - Clínica Geral - R$ 120,00\n 2 - Pediatria - R$ 100,00\n 3 - Ginecologia - R$ 130,00\n 4 - Cardiologia - R$ 150,00\n 5 - Dermatologia - R$ 140,00\n";
        String menuInfoExame = "Célia: \n 1 - Hemograma - R$ 50,00\n 2 - Exames de urina - R$ 30,00\n 3 - Sorologia para hepatite B e C - R$ 80,00\n 0 - Retornar ao menu principal\n";
        String menuInfoVacina = "Célia: \n 1 - Vacina contra COVID-19 - R$ 0,00 (disponível gratuitamente)\n 2 - Vacina MMR (sarampo, caxumba e rubéola) - R$ 80,00\n 3 - Vacina HPV - R$ 150,00\n";
    
    System.out.println(menu1);
    Scanner entrada = new Scanner(System.in);
    int opcao, opcaoMenuAgenda, opcaoMenuMarca, opcaoMenuInfo;
    
do {
    opcao = entrada.nextInt();

    switch (opcao){
        case 1:
            System.out.println(menuAgenda);
            opcaoMenuAgenda = entrada.nextInt();

            switch (opcaoMenuAgenda){
                case 1:
                    System.out.println(menuMarca);
                    opcaoMenuMarca = entrada.nextInt();
                    if (opcaoMenuMarca < 6){
                        System.out.println("Célia: Para marcar sua consulta, informe nome completo do paciente.");
                        entrada.nextLine();
                        String nomePaciente = entrada.nextLine();
                        System.out.println("Célia: Sua consulta com foi marcada com sucesso!");}
                    else {
                        System.out.println("Opção Inválida!");    
                    }
                    break;
                
                case 2:
                    System.out.println("Célia: Para cancelar sua consulta, informe nome completo do paciente.");
                    entrada.nextLine();
                    String nomePaciente = entrada.nextLine(); 
                    System.out.println("Célia: Sua consulta foi cancelada com sucesso!");
                    break;

                case 0:
                    System.out.println("-----------------------");

                    break;

                default: System.out.println("Opção Inválida!");
        }
        
        break;

        case 2:
            System.out.println(menuInfo);
            opcaoMenuInfo = entrada.nextInt();
            switch(opcaoMenuInfo){
                case 1:
                    System.out.println(menuInfoConsulta);
                    break;
                
                case 2:
                    System.out.println(menuInfoExame);
                    break;

                case 3:
                    System.out.println(menuInfoVacina);
                    break;

                case 0:
                    System.out.println("-----------------------");
                    break;
     
            default: System.out.println("Opção Inválida!");   
            }
            
            break;  
             
        case 3: 
            int sair;
            do {
            System.out.println("Célia: Um momento, por favor. Estou conectando você a um atendente. Pressione 0 sair da fila");
            sair = entrada.nextInt();  
            } while (sair != 0);
        
        case 0:
            System.out.println("-----------------------");
            break;
    default: System.out.println("Opção Inválida!");    
    }   
     
    break;    
} while (opcao != 0);
System.out.println("Obrigado por entrar em contato! Se precisar de mais alguma coisa, estou à disposição. Até logo!");
}
}