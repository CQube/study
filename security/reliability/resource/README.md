# .json structure 
 - failure_rate: λ(АО) - интенсивность отказов АС×10^-8, АО - аппартные отказы
    - display: λмн(АО) = мн - монитор 
    - processor: λпр(АО) = пр - процессор
    - memory: λпм(АО) = пм - память
    - power_supply: λбп(АО) = бп - блок питания 
     
 - failure_rate_factor: α – коэффициент интенсивности отказа ПС, принимающий значение в диапазоне 0,1 – 10;
 - beta: β×10
 - time: t×10^4
 - operation_condition_factor: k - кэффициент условий эксплуатации
    - teperature: k(тем)
    - vibration: k(виб)
    - overload: k(пер)
 - storing: xранение
    - storing_time: tх ×10^4 - время хранения
    - fail_rate_drop_factor: G - коэффициент снижения интенсивности отказа при хранении
 - cyclic_work: циклическая работа
    - time: t×10^4
    - storing_time_factor: r - коэффициент времени хранения
 - gamma: γ - процентная наработка до отказа
 - dt: Δt×10^3 
   