#ifndef OPENPOSE_UTILITIES_POINTER_CONTAINER_HPP
#define OPENPOSE_UTILITIES_POINTER_CONTAINER_HPP

namespace op
{
    template<typename TPointerContainer>
    inline bool checkNoNullNorEmpty(const TPointerContainer& tPointerContainer)
    {
        return (tPointerContainer != nullptr && tPointerContainer->size() > 0);
    }

    template<typename TDatumsSP>
    class PointerContainerGreater
    {
    public:
        bool operator() (const TDatumsSP& a, const TDatumsSP& b)
        {
            if (!b || b->empty())
                return true;
            else if (!a || a->empty())
                return false;
            else
                return *(*a)[0] > *(*b)[0];
        }
    };

    template<typename TDatumsSP>
    class PointerContainerLess
    {
    public:
        bool operator() (const TDatumsSP& a, const TDatumsSP& b)
        {
            if (!b || b->empty())
                return false;
            else if (!a || a->empty())
                return true;
            else
                return *(*a)[0] < *(*b)[0];
        }
    };
}

#endif // OPENPOSE_UTILITIES_POINTER_CONTAINER_HPP
