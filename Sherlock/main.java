import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        int i, vida, j;
        boolean exit = false;
        Scanner teclado = new Scanner(System.in);

        while (!exit) {
            System.out.println("|Selecione o cenário que deseja jogar|");
            System.out.println("|------------------------------------|");
            System.out.println("| 1 - A study in pink                |");
            System.out.println("| 2 - The great game                 |");
            System.out.println("| 3 - The Abominable Bride           |");
            System.out.println("| 0 - Sair                           |");
            System.out.println("|------------------------------------|");
            System.out.print("Selecione: ");
            int opcao = teclado.nextInt();
            switch (opcao) {
                case 1:
                    System.out.println("A STUDY IN PINK");
                    System.out.println();
                    String[] suspeitos = {"Sherlock", "Inspetor Lestrage", "Turista", "Arqui-inimigo do Sherlock", "Taxista", "John watson "};
                    String assassino = "taxista";
                    String[] pistas = {"Ela estava se molhando e precisava sair da chuva ",
                            "As demais vítimas estavam atrasadas e precisavam no meio de transporte",
                            "Se rache = vingança em alemão, então o assassino estava se vingando",
                            "A mala da vítima estava no carro do assassino",
                            "As mortes foram coincidencias",
                            "O assassino acredita conseguir ler as pessoas.",
                            "As vitimas estavam em umas regiões em diversas regiões da cidade",
                            "O assassino trabalha na em um cargo relacionado ao estado",
                            "O assassino rapitava as vitimas em areas movimentadas",
                            "O assassino conhece as ruas da cidade muito bem ",
                            "O assassino mora e passa a maior parte do tempo na Baker Street"};

                    String[] solucoes = {"O turista matou", "O inspetor Lestrage matou", "Sherlock matou para ser o único a conseguir 'deduzir' quem é o assassino",
                            "O taxista é o assassino", "O arqui-inimigo do sherlock é o assassino", "John watson assassinou assassinou as vitimas para ver como Shelock iria tentar resolver o caso"};
                    String chute = "";
                    vida = 8;
                    j = 3;

                    Arrays.sort(pistas);
                    for (i = 0; i <= 2; i++) {
                        System.out.printf("Pista %d - ", i + 1);
                        System.out.println(pistas[i]);
                    }

                    while (!chute.equals(assassino) || i <= pistas.length) {
                        if (vida == 0) {
                            System.out.println("\nVocê não tem mais vidas!");
                            System.out.println("Voltando ao menu principal!\n");
                            break;
                        } else {
                            System.out.println("\n1 - Chutar\n2 - Pista\n3 - Ver possiveis soluções e Suspeitos\n0 - Sair\n");
                            System.out.println("Vidas: " + vida);
                            System.out.print("Entrada: ");
                            int opcao2 = teclado.nextInt();

                            if (opcao2 == 1) {
                                System.out.print("Digite o nome do assassino:");
                                chute = teclado.next();
                                int comparacao = chute.toLowerCase(Locale.ROOT).compareTo(assassino);
                                if (comparacao == 0) {
                                    System.out.println("RESPOSTA CORRETA!");
                                    break;
                                } else {
                                    System.out.println("RESPOSTA INCORRETA!");
                                    vida--;
                                }
                            } else if (opcao2 == 2) {
                                if (j < pistas.length) {
                                    for (i = 0; i <= j; i++) {
                                        System.out.printf("Pista %d - ", i + 1);
                                        System.out.println(pistas[i]);
                                    }
                                } else {
                                    System.out.println("Não existem mais pistas!");
                                }
                                j++;
                                vida--;
                            } else if (opcao2 == 3) {
                                System.out.println("Possiveis soluções:\n");
                                for (String k : solucoes) {
                                    System.out.println(k);
                                }
                                System.out.println();
                                System.out.println("Suspeitos:\n");
                                for (String k : suspeitos) {
                                    System.out.print(k + ", ");
                                }
                                System.out.println();
                            } else if (opcao2 == 0) {
                                System.out.print("Obrigado por jogar!");
                                exit = true;
                                break;
                            } else
                                System.out.println("Opcao inexistente!\n");
                        }
                    }
                    break;
                case 2:
                    System.out.println("THE GREAT GAME");
                    System.out.println();
                    String[] suspeitos2 = {"Molly Hopper", "Moriarty", "Marry", "Mycroft", "Sindry"};
                    String solucao = "moriarty";
                    String[] pistas_c2 = {
                            "As demais vítimas precisavam atrasadas e precisavam no meio de transporte",
                            "'M' é a inicial do inimigo de Sherlock",
                            "Ele observa Sherlock a anos",
                            "Possui intelecto tão bom quanto ao de Sherlock",
                            "É considerado o principal inimigo de Sherlock",
                            "'M' é um homem"};

                    String[] solucoes2 = {"Molly Hopper é 'M'", "Moriarty é 'M'", "Marry é 'm'", "Mycroft é 'M'"};
                    chute = "";
                    vida = 8;
                    j = 3;

                    Arrays.sort(pistas_c2);
                    for (i = 0; i <= 2; i++) {
                        System.out.printf("Pista %d - ", i + 1);
                        System.out.println(pistas_c2[i]);
                    }

                    while (!chute.equals(solucao) || i <= pistas_c2.length) {
                        if (vida == 0) {
                            System.out.println("\nVocê não tem mais vidas!");
                            System.out.println("Voltando ao menu principal!\n");
                            break;
                        } else {
                            System.out.println("\n1 - Chutar\n2 - Pista\n3 - Ver possiveis soluções e Suspeitos\n0 - Sair\n");
                            System.out.println("Vidas: " + vida);
                            System.out.print("Entrada: ");
                            int opcao2 = teclado.nextInt();

                            if (opcao2 == 1) {
                                teclado.nextLine();
                                System.out.print("Digite o nome de 'M': ");
                                chute = teclado.next();
                                int comparacao = chute.toLowerCase(Locale.ROOT).compareTo(solucao);
                                if (comparacao == 0) {
                                    System.out.println("RESPOSTA CORRETA!");
                                    break;
                                } else {
                                    System.out.println("RESPOSTA INCORRETA!");
                                    vida--;
                                }
                            } else if (opcao2 == 2) {
                                if (j < pistas_c2.length) {
                                    for (i = 0; i <= j; i++) {
                                        System.out.printf("Pista %d - ", i + 1);
                                        System.out.println(pistas_c2[i]);
                                    }
                                } else {
                                    System.out.println("Não existem mais pistas!");
                                }
                                j++;
                                vida--;
                            } else if (opcao2 == 3) {
                                System.out.println("Possiveis soluções:\n");
                                for (String k : solucoes2) {
                                    System.out.println(k);
                                }
                                System.out.println();
                                System.out.println("Suspeitos:\n");
                                for (String k : suspeitos2) {
                                    System.out.print(k + ", ");
                                }
                                System.out.println();
                            } else if (opcao2 == 0) {
                                System.out.print("Obrigado por jogar!");
                                exit = true;
                                break;
                            } else {
                                System.out.println("Opcao inexistente!\n");
                            }
                        }
                    }
                    break;
                case 3:
                    System.out.println("THE ABOMINABLE BRIDE");
                    System.out.println();
                    String[] resolucoes_c3 = {"Moriarty esta vivo", "Moriarty esta morto", "Ricoletti morreu com o tiro", "Ricoletti não morreu com o tiro"};
                    String[] pistas_c3 = {"Moriarty deu um tiro na boca",
                            "Ricoletti levou um tiro na nuca",
                            "O casos foram alucinações causadas pela cocaina",
                            "Moriarty não achava ruim morrer mas continuar causando problemas",
                            "O video de Moriarty dizendo 'Sentiu minha falta' não é fake",
                            "Moriarty sempre se preparava para todos os cenarios",
                            "Sherlock não tinha usado cocaina para tentar solucinar o caso",
                            "A dedução de Sherlock de trocar o corpo por um cadaver real estava errada",
                            "O caso Ricoletti foi uma imaginação de Sherlock",
                            "O caso Moriarty e Ricoletti são muito semenhantes nos principais pontos"};

                    String[] solucoes_c3 = {"Somente Moriarty está morto", "Somente Moriarty está vivo", "Moriarty e Ricoletti morreram com o tiro", "Moriarty e Ricoletti nao morreram com o tiro"};
                    vida = 8;
                    j = 3;

                    Arrays.sort(pistas_c3);
                    for (i = 0; i <= 2; i++) {
                        System.out.printf("Pista %d - ", i + 1);
                        System.out.println(pistas_c3[i]);
                    }

                    while (i <= pistas_c3.length) {
                        if (vida == 0) {
                            System.out.println("\nVocê não tem mais vidas!");
                            System.out.println("Voltando ao menu principal!\n");
                            break;
                        } else {
                            System.out.println("\n1 - Chutar\n2 - Pista\n3 - Ver possiveis soluções e Suspeitos\n0 - Sair\n");
                            System.out.println("Vidas: " + vida);
                            System.out.print("Entrada: ");
                            int opcao3 = teclado.nextInt();

                            if (opcao3 == 1) {
                                System.out.println("Selecione a resposta correta:");
                                System.out.println("|--------------------------------------------------");
                                for (i = 0; i < solucoes_c3.length; i++) {
                                    System.out.printf("| %d - %s\n", (i + 1), solucoes_c3[i]);
                                }
                                System.out.println("|--------------------------------------------------");
                                System.out.print("Entrada: ");
                                int resposta = teclado.nextInt();
                                if (resposta == 3) {
                                    System.out.println("RESPOSTA CORRETA!");
                                    break;
                                } else {
                                    System.out.println("RESPOSTA INCORRETA!");
                                    vida--;
                                }
                            } else if (opcao3 == 2) {
                                if (j < pistas_c3.length) {
                                    for (i = 0; i <= j; i++) {
                                        System.out.printf("Pista %d - ", i + 1);
                                        System.out.println(pistas_c3[i]);
                                    }
                                } else {
                                    System.out.println("Não existem mais pistas!");
                                }
                                j++;
                                vida--;
                            } else if (opcao3 == 3) {
                                System.out.println("Possiveis soluções:\n");
                                for (String k : solucoes_c3) {
                                    System.out.println(k);
                                }
                                System.out.println();
                                System.out.println("Suspeitos:\n");
                                for (String k : resolucoes_c3) {
                                    System.out.print(k + ", ");
                                }
                                System.out.println();
                            } else if (opcao3 == 0) {
                                System.out.print("Obrigado por jogar!");
                                exit = true;
                                break;
                            } else {
                                System.out.println("Opcao inexistente!\n");
                            }
                        }
                    }
                    break;
                default:
                    System.out.print("Obrigado por jogar!");
                    exit = true;
                    break;
            }
        }
    }
}
