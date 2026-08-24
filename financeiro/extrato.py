from datetime import datetime

from financeiro.fechamento import Fechamento
from financeiro.lancamento import Lancamento
from financeiro.conciliacao import Conciliacao


class Extrato:
    def __init__(self, mes: int, ano: int) -> None:
        if not 1 <= mes <= 12:
            raise ValueError("Mês inválido")
        self.mes = mes
        self.ano = ano
        self.fechamentos: list[Fechamento] = []

    def adicionarFechamento(self, fechamento: Fechamento) -> None:
        if not isinstance(fechamento, Fechamento):
            raise TypeError("Fechamento inválido")
        self.fechamentos.append(fechamento)

    def _lancamentos_do_periodo(self) -> list[Lancamento]:
        lancamentos = []
        for fechamento in self.fechamentos:
            for lancamento in fechamento.getFechamentos():
                data = datetime.strptime(lancamento.data, "%d/%m/%Y")
                if data.month == self.mes and data.year == self.ano:
                    lancamentos.append(lancamento)
        return lancamentos

    def total_lancamentos(self) -> int:
        return len(self._lancamentos_do_periodo())

    def total_debitos(self) -> float:
        return sum(l.valor for l in self._lancamentos_do_periodo() if l.tipo == "debito")

    def total_creditos(self) -> float:
        return sum(l.valor for l in self._lancamentos_do_periodo() if l.tipo == "credito")

    def saldo_final(self) -> float:
        return self.total_creditos() - self.total_debitos()

    def possui_conciliacao_pendente(self) -> bool:
        lancamentos = self._lancamentos_do_periodo()
        debitos = [l for l in lancamentos if l.tipo == "debito"]
        creditos = [l for l in lancamentos if l.tipo == "credito"]
        conciliacao = Conciliacao(debitos, creditos)
        return not conciliacao.verifica_conciliacao()

    def resumo(self) -> dict:
        return {
            "periodo": f"{self.mes:02d}/{self.ano}",
            "total_lancamentos": self.total_lancamentos(),
            "total_debitos": self.total_debitos(),
            "total_creditos": self.total_creditos(),
            "saldo_final": self.saldo_final(),
            "conciliacao_pendente": self.possui_conciliacao_pendente(),
        }

    def __repr__(self) -> str:
        return f"Extrato {self.mes:02d}/{self.ano}"