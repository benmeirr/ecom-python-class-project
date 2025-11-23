from typing import Optional, List

from model.customer import Customer
from model.customer_status import CustomerStatus
from repository import customer_repository


async def get_customer_by_id(customer_id: int) -> Optional[Customer]:
    return await customer_repository.get_by_id(customer_id)


async def get_all_customers() -> List[Customer]:
    return await customer_repository.get_all()


async def create_customer(customer: Customer) -> int:
    if customer.status == CustomerStatus.VIP:
        vip_customers = await customer_repository.get_by_status(CustomerStatus.VIP)
        if len(vip_customers) < 10:
            return await customer_repository.create_customer(customer)
        else:
            raise Exception("Can't create new VIP customer - out of limit")
    else:
        return await customer_repository.create_customer(customer)